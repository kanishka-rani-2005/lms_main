from django.contrib import admin
from django.urls import path,include
from AddNotice import views

urlpatterns = [
    path('',views.addnotice,name='addnotice')
]
