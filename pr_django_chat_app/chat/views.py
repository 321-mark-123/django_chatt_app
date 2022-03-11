from django.shortcuts import render
from .models import Message
# Create your views here.


def index(request):
    # print("received Data" + request.POST['textmessage'])
    Message.objects.create(text=request.POST['textmessage'], chat=None, author=request.user, receiver=request.user
                           )
    return render(request, 'chat/index.html', {'username': 'mark'})
