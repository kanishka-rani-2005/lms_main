from django.shortcuts import render,redirect
from NoticeBoard.models import Notice


# Create your views here.
def addnotice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')


        Notice.objects.create(
            title=title,
            details=details
        )

        return redirect('/notice')
    return render(request, 'addnotice/addnotice.html')



