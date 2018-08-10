from django.shortcuts import render


def welcome(request):
    return render(request, 'grampanchayatSaravali\index.html')


