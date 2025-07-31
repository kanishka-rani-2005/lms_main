from django.shortcuts import render
from django.http import HttpResponse
from Books.models import Book
# Create your views here.


def home(request):
    return render(request,'books/home.html')

def books(request):
    data = Book.objects.all()
    books={
        'details':data
    }
    return render(request,'books/books.html',context=books)

