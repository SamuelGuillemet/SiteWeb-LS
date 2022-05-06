from django.shortcuts import render
from django.urls import reverse
from .models import Article, Theme
from django.views import generic
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    queryset = createFilter(request)
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    theme_list = [field.name for field in Theme._meta.get_fields()][2::]
    publi_list = [c[0] for c in Article.publication.field.choices]
    breadcrumbs_list = [
        {'link': reverse('HomePage:home'),
         'text': "Accueil"
         },
        {'link': reverse('ArticlePage:home'),
         'text': "Articles"
         }
    ]

    context = {
        'page_obj': page_obj,
        'article_list': queryset,
        'theme_list': theme_list,
        'publi_list': publi_list,
        'breadcrumbs_list': breadcrumbs_list
    }
    return render(request, 'ArticlePage/index.html', context)


def createFilter(request):
    theme_list = [field.name for field in Theme._meta.get_fields()][2::]
    queryset = Article.objects.all().order_by('-published_date')
    if request.method == 'GET':
        parameters = request.GET.keys()
        if parameters is not None:
            Q_filter1 = Q()
            Q_filter2 = Q()
            for para in parameters:
                if para == 'publication':
                    filter = {para: request.GET.get(para, None)}
                    Q_filter1 = Q(**filter) | Q_filter1
                elif para in theme_list:
                    value = request.GET.get(para, None) == 'True'
                    filter = {'theme__{}'.format(para): value}
                    Q_filter2 = Q(**filter) | Q_filter2
            queryset = queryset.filter(Q_filter1 & Q_filter2)
            return queryset


class DetailView(generic.DetailView):
    model = Article
    template_name = 'ArticlePage/detail.html'

    def get_queryset(self):
        return Article.objects.filter(published_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        breadcrumbs_list = [
            {
                'link': reverse('HomePage:home'),
                'text': "Accueil"
            },
            {
                'link': reverse('ArticlePage:home'),
                'text': "Articles"
            },
            {
                'link': reverse('ArticlePage:detail', args=(self.kwargs['pk'],)),
                'text': self.get_object().title
            }
        ]
        theme_list = [field.name for field in Theme._meta.get_fields()][2::]
        context = super().get_context_data(**kwargs)
        context['theme_list'] = theme_list
        context['breadcrumbs_list'] = breadcrumbs_list
        if self.request.user.is_authenticated:
            context['modify'] = True
        return context
