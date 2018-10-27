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


def photoGallery(request):
    return render(request, 'grampanchayatSaravali/gallery.html')


def faq(request):
    return render(request, 'grampanchayatSaravali/contact.html')


def developmentPlan(request):
    return render(request, 'grampanchayatSaravali/vikasArakhada.html')


def committees(request):
    return render(request, 'grampanchayatSaravali/committees.html')


def scm1(request):
    return render(request, 'grampanchayatSaravali/scm1.html')


def scm2(request):
    return render(request, 'grampanchayatSaravali/scm2.html')


def scm3(request):
    return render(request, 'grampanchayatSaravali/scm3.html')


def scm4(request):
    return render(request, 'grampanchayatSaravali/scm4.html')


def scm5(request):
    return render(request, 'grampanchayatSaravali/scm5.html')


def scm6(request):
    return render(request, 'grampanchayatSaravali/scm6.html')


def about(request):
    return render(request, 'grampanchayatSaravali/about.html')



def other1(request):
    return render(request, 'grampanchayatSaravali/other1.html')

def other2(request):
    return render(request, 'grampanchayatSaravali/other2.html')

def other3(request):
    return render(request, 'grampanchayatSaravali/other3.html')

def other4(request):
    return render(request, 'grampanchayatSaravali/other4.html')

def other5(request):
    return render(request, 'grampanchayatSaravali/other5.html')

def other6(request):
    return render(request, 'grampanchayatSaravali/other6.html')


def other7(request):
    return render(request, 'grampanchayatSaravali/other7.html')