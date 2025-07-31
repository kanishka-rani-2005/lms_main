from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'books/home.html')

def books(request):
    details={
        'title':'Complete Python Course',
        'author':'Kode gurukul',
        'publisher':'Kode gurukul'
    }
    return render(request,'books/books.html',context=details)

