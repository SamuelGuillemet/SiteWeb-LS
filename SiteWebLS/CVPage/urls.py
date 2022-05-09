from django.urls import path
from . import views

app_name = 'CVPage'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail')
]
