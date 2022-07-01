from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def home(request):
    breadcrumbs_list = [
        {'link': reverse('HomePage:home'),
         'text': "Accueil"
         },
        {'link': reverse('GalleryPage:home'),
         'text': "Galerie photos"
         }
    ]

    context = {
        'breadcrumbs_list': breadcrumbs_list
    }
    return render(request, 'GalleryPage/index.html', context)
