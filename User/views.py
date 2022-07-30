from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
# Create your views here.
from User import models

from User.models import WangUser


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj_user = models.WangUser.objects.filter(username=username, password=password)
        print(username)

        print(obj_user)
        if obj_user:
            return render(request, 'index.html', {'username': username})
        error = '用户名和密码错误'

    return render(request, 'login.html', locals(), )


@login_required
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_list = models.WangUser.objects.filter(username=username)
        error_name = []
        if user_list:
            error_name = '用户名已经存在'
            return render(request, 'register.html', {'error_name': error_name})
        else:
            username = models.WangUser.objects.create(username=username, password=password, email=email)
            username.save()
            return redirect('login')
    return render(request, 'register.html')


# Create your views here.


def setting(request):
    username = request.POST.get('username')
    print(username)
    return render(request, 'setting.html',{'username':username})
