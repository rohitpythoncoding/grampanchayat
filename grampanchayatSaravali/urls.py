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
    path('photoGallery/', views.photoGallery, name='photoGallery'),
    path('faq/', views.faq, name='faq'),
    path('developmentPlan/', views.developmentPlan, name='developmentPlan'),
    path('other/', views.other, name='other'),
    path('committees/', views.committees, name='committees'),
    path('scm1/', views.scm1, name='scm1'),
    path('scm2/', views.scm2, name='scm2'),
    path('scm3/', views.scm3, name='scm3'),
    path('scm4/', views.scm4, name='scm4'),
    path('scm5/', views.scm5, name='scm5'),
    path('scm6/', views.scm6, name='scm6'),

]