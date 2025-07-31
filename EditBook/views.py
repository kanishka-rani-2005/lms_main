from django.shortcuts import render,redirect
from Books.models import Book


# Create your views here.
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        edition = request.POST.get('edition')
        price = request.POST.get('price')
        pages = request.POST.get('pages')


        Book.objects.create(
            title=title,
            author=author,
            publisher=publisher,
            edition=edition,
            price=price,
            pages=pages
        )
        return redirect('/books')
    return render(request, 'updatebook/addbook.html')