from django.shortcuts import render
from .models import Article, Theme
from django.views import generic
from django.db.models import Q

# Create your views here.


def home(request):
    queryset = createFilter(request)
    theme_list = [field.name for field in Theme._meta.get_fields()][2::]
    publi_list = [c[0] for c in Article.publication.field.choices]
    context = {
        'article_list': queryset,
        'theme_list': theme_list,
        'publi_list': publi_list
    }
    return render(request, 'ArticlePage/index.html', context)


def createFilter(request):
    queryset = Article.objects.all()
    if request.method == 'GET':
        parameters = request.GET.keys()
        if parameters is not None:
            Q_filter1 = Q()
            Q_filter2 = Q()
            for para in parameters:
                if para == 'publication':
                    filter = {para: request.GET.get(para, None)}
                    Q_filter1 = Q(**filter) | Q_filter1
                else:
                    value = request.GET.get(para, None) == 'True'
                    filter = {'theme__{}'.format(para): value}
                    Q_filter2 = Q(**filter) | Q_filter2
            qo = Q_filter1 & Q_filter2
            queryset = queryset.filter(Q_filter1 & Q_filter2)
            return queryset
