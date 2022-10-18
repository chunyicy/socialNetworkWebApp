from django.shortcuts import render

from .models import Message

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    # get information from the url
    # set it to Anonymous if the username field has nothing fill out
    username = request.GET.get('username', 'Anonymous')
    # show the saved message for a room
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})