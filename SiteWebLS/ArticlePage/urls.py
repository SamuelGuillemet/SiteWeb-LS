from django.urls import path
from . import views

app_name = 'ArticlePage'
urlpatterns = [
    path('', views.home, name='home'),
]
