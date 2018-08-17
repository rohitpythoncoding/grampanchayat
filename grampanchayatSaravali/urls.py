from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    url('home/', views.home),
    path('contact/', views.contact),
]
