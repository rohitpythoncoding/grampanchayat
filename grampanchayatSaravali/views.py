from django.shortcuts import render


def welcome(request):
    language = request.GET.get('language')
    if not language:
        print("First value of language", language)
        request.session['lang'] = "en"
        print("will show page in English")
    # request.session['lang'] = language
    if language and language == "marathi":
        print("This time for marathi")
        request.session['lang'] = "marathi"
    # elif language and language == 'marathi':
    #     request.session['lang'] = "marathi"
    print(language)
    return render(request, 'grampanchayatSaravali/index.html')


def home(request):
    return render(request, 'grampanchayatSaravali/index.html')


def aboutVillage(request):
    return render(request, 'grampanchayatSaravali/about.html')


def workers(request):
    return render(request, 'grampanchayatSaravali/workers.html')


def map(request):
    return render(request, 'grampanchayatSaravali/index.html')


def services(request):
    return render(request, 'grampanchayatSaravali/index.html')


def electedMember(request):
    return render(request, 'grampanchayatSaravali/electedMember.html')


def missionVision(request):
    return render(request, 'grampanchayatSaravali/index.html')


def schemes(request):
    return render(request, 'grampanchayatSaravali/index.html')


def photoGallery(request):
    return render(request, 'grampanchayatSaravali/index.html')


def faq(request):
    return render(request, 'grampanchayatSaravali/index.html')