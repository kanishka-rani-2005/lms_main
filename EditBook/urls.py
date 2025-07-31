from django.contrib import admin
from django.urls import path,include
from EditBook import views




urlpatterns = [
    path("",views.addbook,name='addbook')
]