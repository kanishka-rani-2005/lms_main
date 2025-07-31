

from django.contrib import admin
from django.urls import path,include
from Books import views

urlpatterns = [
    path('',views.home,name='home'),
    path('books/',views.books,name='books')
]