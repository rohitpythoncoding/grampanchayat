from django.shortcuts import render


def welcome(request):
    return render(request, 'grampanchayatSaravali\index.html')


def home(request):
    return render(request, 'grampanchayatSaravali\index.html')


def contact(request):
    return render(request, 'grampanchayatSaravali\contact.html')


