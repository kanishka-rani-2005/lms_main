from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def notice(request):
    return render(request,'notice_board/notice_board.html')