from django.utils import timezone
from django.shortcuts import render
from ArticlePage.models import Article, Theme
from django.views.generic import TemplateView
from PodcastPage.models import Podcast
from .mixins import SearchMixin
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    queryset = Article.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')[:4]
    podcasts = Podcast.objects.all()[:2]
    paginator = Paginator(podcasts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'article_list': queryset,
        'page_obj': page_obj,
    }
    return render(request, 'HomePage/index.html', context)


class GlobalSearchView(SearchMixin, TemplateView):
    template_name = 'HomePage/global_search.html'
    search_settings = {
        'ArticlePage.Article': ['title', 'author', 'article'],
        'CVPage.CV': ['nom', 'prenom']
    }

    def get_context_data(self, **kwargs):
        theme_list = [field.name for field in Theme._meta.get_fields()][2::]
        context = super().get_context_data(**kwargs)
        context['theme_list'] = theme_list
        return context
