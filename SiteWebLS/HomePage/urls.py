from django.urls import path
from . import views

app_name = 'HomePage'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.GlobalSearchView.as_view(), name='search')
]
