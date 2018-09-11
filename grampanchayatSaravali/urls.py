from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('home/', views.home, name='home'),
    path('aboutVillage/', views.aboutVillage, name='aboutVillage'),
    path('services/', views.services, name='services'),
    path('map/', views.map, name='map'),
    path('workers/', views.workers, name='workers'),
    path('electedMember/', views.electedMember, name='electedMember'),
    path('schemes/', views.schemes, name='schemes'),
    path('missionVision/', views.missionVision, name='missionVision'),
    path('photoGallery/', views.photoGallery, name='photoGallery'),
    path('faq/', views.faq, name='faq'),
]