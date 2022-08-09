from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Photo

# Create your views here.


def home(request):
    queryset = Photo.objects.all()
    
    breadcrumbs_list = [
        {'link': reverse('HomePage:home'),
         'text': "Accueil"
         },
        {'link': reverse('GalleryPage:home'),
         'text': "Galerie photos"
         }
    ]

    context = {
        'photo_list': queryset,
        'breadcrumbs_list': breadcrumbs_list
    }
    return render(request, 'GalleryPage/index.html', context)

def detail(request, id): 
    photo = get_object_or_404(Photo, pk=id)
    breadcrumbs_list = [
        {
            'link': reverse('HomePage:home'),
            'text': "Accueil"
        },
        {
            'link': reverse('GalleryPage:home'),
            'text': "Galerie photos"
        },
        {
            'link': reverse('GalleryPage:detail', args=[photo.pk]),
            'text': photo
        }
    ]
        
    context = {
            'photo': photo,
            'breadcrumbs_list': breadcrumbs_list
    }
        
    return render(request, 'GalleryPage/detail.html', context)