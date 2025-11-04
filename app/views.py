from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Asosiy sahifa")

def search(request):
    info = request.GET.get('q')

    return HttpResponse(f"{info} qidirilmoqda ...")