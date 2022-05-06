from django.apps import apps
from django.db.models import Q
from functools import reduce
from operator import or_


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
