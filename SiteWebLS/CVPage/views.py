from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import CV


# Create your views here.


def home(request):
    queryset = CV.objects.all()
    breadcrumbs_list = [
        {
            'link': reverse('HomePage:home'),
            'text': "Accueil"
        },
        {
            'link': reverse('CVPage:home'),
            'text': "CV"
        }
    ]
    context = {
        'cv_list': queryset,
        'breadcrumbs_list': breadcrumbs_list
    }
    return render(request, 'CVPage/index.html', context=context)


def detail(request, id):
    cv = get_object_or_404(CV, pk=id)
    breadcrumbs_list = [
        {
            'link': reverse('HomePage:home'),
            'text': "Accueil"
        },
        {
            'link': reverse('CVPage:home'),
            'text': "CV"
        },
        {
            'link': reverse('CVPage:detail', args=[cv.pk]),
            'text': cv
        }
    ]
    if request.user.is_authenticated:
        modify = True
        modify_link = reverse('admin:CVPage_cv_change', args=[cv.pk])

    context = {
        'cv': cv,
        'breadcrumbs_list': breadcrumbs_list,
        'modify': modify,
        'modify_link': modify_link
    }

    return render(request, 'CVPage/detail.html', context=context)
