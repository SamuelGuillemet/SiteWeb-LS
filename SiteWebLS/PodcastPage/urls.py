from django.urls import path
from . import views

app_name = 'PodcastPage'
urlpatterns = [
    path('', views.home, name='home'),
]
