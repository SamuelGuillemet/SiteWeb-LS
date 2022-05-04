from django.utils import timezone
from django.shortcuts import render
from ArticlePage.models import Article

# Create your views here.


def home(request):
    queryset = Article.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')[:4]
    context = {
        'article_list': queryset
    }
    return render(request, 'HomePage/index.html', context)
