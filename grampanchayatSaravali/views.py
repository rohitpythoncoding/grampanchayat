from django.shortcuts import render


def welcome(request):
    request.session['lang'] = 'en'
    return render(request, 'grampanchayatSaravali/index.html')


def home(request):
    # if request.session['name'] == 'Superman':
    #     print(request.session['name'], 'is awesome!!!!!!!')
    return render(request, 'grampanchayatSaravali/index.html')


def workers(request):
    return render(request, 'grampanchayatSaravali/workers.html')


def certificates(request):
    return render(request, 'grampanchayatSaravali/certificates.html')


def map(request):
    return render(request, 'grampanchayatSaravali/index.html')


def services(request):
    return render(request, 'grampanchayatSaravali/index.html')


def electedMember(request):
    return render(request, 'grampanchayatSaravali/electedMember.html')


def schemes(request):
    return render(request, 'grampanchayatSaravali/schemes.html')


def photoGallery(request):
    return render(request, 'grampanchayatSaravali/index.html')


def faq(request):
    return render(request, 'grampanchayatSaravali/contact.html')


def developmentPlan(request):
    return render(request, 'grampanchayatSaravali/vikasArakhada.html')

def other(request):
    return render(request, 'grampanchayatSaravali/other.html')

def committees(request):
    return render(request, 'grampanchayatSaravali/committees.html')