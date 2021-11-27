from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

from scrumboard.models import User2, Message


def usersPageFunction (request):

    username = request.POST.get('username')
    print(username)
    if username is not None:
        return redirect('/?username=' + username)
    else:
        return render(request, 'usersPage.html')

def loginPage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user2 = authenticate(request, username=username, password=password)

        queryset = User2.objects.all()
        for user in queryset:
            if user.username == username and user.password == password:
                login(request, user2)
                return redirect('usersPageFunction')
            else:
                messages.info(request, 'Username or password incorect')
    context = {}
    return render(request, 'login.html' ,context)

def chat (request):
    username = request.GET.get('username')
    print("username:"+username)
    return render(request, 'chat.html' ,{
        'username':username
    })

def send (request):
    username = request.POST['username']
    print(username)
    message = request.POST['message']
    print(message)
    newMessage = Message.objects.create(message=message,user=username)
    newMessage.save()

    return HttpResponse('SUCCESS')


def seeChat (request):
    messages =Message.objects.all()
    return JsonResponse({'messages':list(messages.values())})
# Create your views here.
