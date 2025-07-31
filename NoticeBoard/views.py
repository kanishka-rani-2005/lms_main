from django.shortcuts import render
from django.http import HttpRequest
from NoticeBoard.models import Notice
# Create your views here.

def notice(request):
    data = Notice.objects.all()
    notices={
        'notices':data
    }
    return render(request,'notice_board/notice_board.html',context=notices)