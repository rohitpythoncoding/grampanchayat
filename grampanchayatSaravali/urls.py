from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('map/', views.map, name='map'),
    path('workers/', views.workers, name='workers'),
    path('electedMember/', views.electedMember, name='electedMember'),
    path('certificates/', views.certificates, name='certificates'),
    path('schemes/', views.schemes, name='schemes'),
    path('photoGallery/', views.photoGallery, name='photoGallery'),
    path('faq/', views.faq, name='faq'),
    path('developmentPlan/', views.developmentPlan, name='developmentPlan'),
]