from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    queryset = models.CV.objects.all()
    context = {
        'cv_list': queryset
    }
    return render(request, 'CVPage/index.html', context=context)
