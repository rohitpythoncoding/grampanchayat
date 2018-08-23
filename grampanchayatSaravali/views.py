from django.shortcuts import render


def welcome(request):
    request.session['lang'] = 'marathi'
    return render(request, 'grampanchayatSaravali/index.html')


def home(request):
    if request.session['name'] == 'Superman':
        print(request.session['name'], 'is awesome!!!!!!!')
    return render(request, 'grampanchayatSaravali/index.html')


def aboutVillage(request):
    return render(request, 'grampanchayatSaravali/about.html')


def contact(request):
    return render(request, 'grampanchayatSaravali/contact.html')


def map(request):
    return render(request, 'grampanchayatSaravali/index.html')


def services(request):
    return render(request, 'grampanchayatSaravali/index.html')


def electedMember(request):
    return render(request, 'grampanchayatSaravali/index.html')


def missionVision(request):
    return render(request, 'grampanchayatSaravali/index.html')


def schemes(request):
    return render(request, 'grampanchayatSaravali/index.html')


def photoGallery(request):
    return render(request, 'grampanchayatSaravali/index.html')


def faq(request):
    return render(request, 'grampanchayatSaravali/index.html')