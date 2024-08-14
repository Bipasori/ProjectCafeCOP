from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from user.models import User

def index(request):
    context = {}
    users = User.objects.filter()

    print("***********************************")
    # print(users)

    context['users'] = users
    context['mymessage'] = 'Welcome...'
    return render(request, 'index.html', context)


def myregister(request):
    context = {}

    print(request)

    user_name = request.GET['user_name']
    user_email = request.GET['user_email']
    user_pwd = request.GET['user_pwd']

    try:
        user = User.objects.get(username=user_name)
        context['mymessage'] = '사용자가 있습니다.'
    except:
        context['mymessage'] = '유효한 사용자입니다. 등록'
        user = User.objects.create_user(user_name,
                                        user_email,
                                        user_pwd)

    return render(request, "index.html", context)


def mylogin(request):
    context = {}

    user_name = request.GET['user_name']
    user_pwd = request.GET['user_pwd']

    user = authenticate(username=user_name, password=user_pwd)
    if user is not None:
        login(request, user)
        context['mymessage'] = '로그인 성공...'

    else:
        context['mymessage'] = '로그인 실패...'

    return render(request, "index.html", context)

def mychange(request):
    context = {}

    user_name = request.GET['user_name']
    user_pwd = request.GET['user_pwd']

    user = User.objects.get(username=user_name)
    user.set_password(user_pwd)
    user.save()

    return render(request, "index.html", context)


def mylogout(request):
    context = {}

    logout(request)

    context['mymessage'] = '로그아웃 되었습니다.'
    return render(request, "index.html", context)


def test1(request):
    raise Exception