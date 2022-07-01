from django.apps import apps
from django.db.models import Q
from functools import reduce
from operator import or_
import os
from django.utils.deprecation import MiddlewareMixin


class SearchMixin:
    search_keyword_arg = 'q'
    search_settings = {}
    lookup_expr = 'icontains'

    def get_search_term(self):
        a = self.request.GET.get(self.search_keyword_arg).split(' ')
        return a
        # return self.request.GET.get(self.search_keyword_arg)

    def build_search_query(self, model_ref, term):
        a = [reduce(or_, [Q(**{f'{field}__{self.lookup_expr}': test})
                    for field in self.search_settings[model_ref]]) for test in term]
        return reduce(or_, a)
        # return reduce(or_, [Q(**{f'{field}__{self.lookup_expr}': term}) for field in self.search_settings[model_ref]])

    def get_search_results(self):
        has_search_result = False
        search_term = self.get_search_term()
        if not search_term:
            return {'has_search_result': has_search_result}

        results = {}

        for model_ref, fields in self.search_settings.items():
            app_name, model_str = model_ref.split('.')
            ModelKlass = apps.get_model(
                app_label=app_name, model_name=model_str)
            qs = ModelKlass.objects.filter(
                self.build_search_query(model_ref, search_term))
            results[model_ref.replace('.', '_').lower()] = qs
            if has_search_result is False and qs.exists():
                has_search_result = True

        results['has_search_result'] = has_search_result
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_result'] = self.get_search_results()
        return context


class RangesMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code != 200 or not hasattr(response, 'file_to_stream'):
            return response
        http_range = request.META.get('HTTP_RANGE')
        if not (http_range and http_range.startswith('bytes=') and http_range.count('-') == 1):
            return response
        if_range = request.META.get('HTTP_IF_RANGE')
        if if_range and if_range != response.get('Last-Modified') and if_range != response.get('ETag'):
            return response
        f = response.file_to_stream
        statobj = os.fstat(f.fileno())
        start, end = http_range.split('=')[1].split('-')
        if not start:  # requesting the last N bytes
            start = max(0, statobj.st_size - int(end))
            end = ''
        start, end = int(start or 0), int(end or statobj.st_size - 1)
        assert 0 <= start < statobj.st_size, (start, statobj.st_size)
        end = min(end, statobj.st_size - 1)
        f.seek(start)
        old_read = f.read
        f.read = lambda n: old_read(min(n, end + 1 - f.tell()))
        response.status_code = 206
        response['Content-Length'] = end + 1 - start
        response['Content-Range'] = 'bytes %d-%d/%d' % (
            start, end, statobj.st_size)
        return response
