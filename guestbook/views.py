from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook.models import Guestbook

# Create your views here.

def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')    #리스트 나옴
    context = {'guestbook_list' : guestbook_list}
    return render(request, 'guestbook/index.html', context)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']
    #레그 데잇은 세팅안해도 된다 트루라서 자동으로 된다.

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    data = request.GET.get('id', None)
    return render(request, 'guestbook/deleteform.html', {'id' : data})


def delete(request):
    Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()
    return HttpResponseRedirect('/guestbook')
    # objects에서 골라내야한다.
    # select제외하고 HttpResponseRedirect를 쓴다