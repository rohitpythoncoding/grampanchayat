from django.shortcuts import render


def welcome(request):
    return render(request, 'grampanchayatSaravali/index.html')


def home(request):
    return render(request, 'grampanchayatSaravali/index.html')


def aboutus(request):
    return render(request, 'grampanchayatSaravali/about.html')


def contact(request):
    return render(request, 'grampanchayatSaravali/contact.html')


def news(request):
    return render(request, 'grampanchayatSaravali/news.html')


def services(request):
    return render(request, 'grampanchayatSaravali/services.html')
