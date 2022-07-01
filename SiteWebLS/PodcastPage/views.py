from django.shortcuts import render
from django.urls import reverse
from .models import Podcast, Theme
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    queryset = Podcast.objects.all()
    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    theme_list = [field.name for field in Theme._meta.get_fields()][2::]
    breadcrumbs_list = [
        {'link': reverse('HomePage:home'),
         'text': "Accueil"
         },
        {'link': reverse('PodcastPage:home'),
         'text': "Podcasts"
         },
        {
            'link': '#',
            'text': page_obj[0].title
        }
    ]

    context = {
        'page_obj': page_obj,
        'theme_list': theme_list,
        'breadcrumbs_list': breadcrumbs_list,
    }

    return render(request, 'PodcastPage/index.html', context)
