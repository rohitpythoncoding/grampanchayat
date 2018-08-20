from django.shortcuts import render


def welcome(request):
    request.session['lang'] = 'lem'
    a = u'\u0905'
    # print(request.session['name'], " is here")
    return render(request, 'grampanchayatSaravali/index.html', {'a': a})


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