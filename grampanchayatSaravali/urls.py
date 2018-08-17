from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('home/', views.home, name='home'),
    path('aboutus/', views.home, name='aboutus'),
    path('services/', views.home, name='services'),
    path('news/', views.home, name='news'),
    path('contact/', views.home, name='contact'),
]