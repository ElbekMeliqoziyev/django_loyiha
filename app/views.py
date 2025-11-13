from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

def home(request):
    book = Book.objects.all()
    data = {'book':book}
    return render(request, "home.html", context=data)

def info(request,id):
    book = Book.objects.get(id=id)
    return render(request, "detail.html", context={'book':book})

def search(request):
    info = request.GET.get('q')

    return HttpResponse(f"{info} qidirilmoqda ...")