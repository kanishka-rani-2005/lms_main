from django.contrib import admin
from django.urls import path,include
from NoticeBoard import views

urlpatterns = [
    path('',views.notice,name='notice')
]