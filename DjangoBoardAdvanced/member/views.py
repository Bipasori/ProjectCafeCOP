from django.shortcuts import render
from member.models import Member

from django.shortcuts import redirect

from datetime import datetime

import requests
import json

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

def member_register(request):
    return render(request, "member_register.html", )

@csrf_exempt
def member_idcheck(request):
    context = {}
    memberid = request.GET['member_id']

    rs = Member.objects.filter(member_id=memberid)

    if(len(rs) > 0):
        context['flag'] = '1'
        context['result_msg'] = '아이디가 있습니다.'
    else:
        context['flag'] = '0'
        context['result_msg'] = '사용 가능한 아이디 입니다.'

    return JsonResponse(context, content_type="application/json")

@csrf_exempt
def member_insert(request):
    context = {}
    memberid = request.GET['member_id']
    memberpwd = request.GET['member_pwd']
    membername = request.GET['member_name']
    memberemail = request.GET['member_email']

    rs = Member.objects.create(member_id=memberid,
                               member_pwd=memberpwd,
                               member_name=membername,
                               member_email=memberemail,
                               register_date=datetime.now())

    context['flag'] = '1'
    context['result_msg'] = '회원가입 되었습니다.<br>Home에서 로그인하세요.'

    return JsonResponse(context, content_type="application/json")

@csrf_exempt
def member_login(request):
    context = {}
    memberid = request.GET['member_id']
    memberpwd = request.GET['member_pwd']

    print(memberid)
    print(memberpwd)

    if 'member_no' in request.session:
        context['flag'] = '1'
        context['result_msg'] = 'Login 되어 있습니다.'
    else:

        rsTmp = Member.objects.filter(member_id=memberid, member_pwd=memberpwd)

        if rsTmp:
            # Session에 member_no를 저장
            rsMember = Member.objects.get(member_id=memberid, member_pwd=memberpwd)
            memberno = rsMember.member_no
            membername = rsMember.member_name
            rsMember.access_latest = datetime.now()
            rsMember.save()

            request.session['member_no'] = memberno
            request.session['member_name'] = membername

            context['flag'] = '0'
            context['result_msg'] = 'Login 성공... '
        else:
            context['flag'] = '1'
            context['result_msg'] = 'Login error... 아이디와 비번을 확인하세요.'

    return JsonResponse(context, content_type="application/json")


def member_logout(request):
    context = {}

    request.session.flush()

    return redirect('/')


def member_edit(request):
    context = {}

    if 'member_no' in request.session:
        memberno = request.session['member_no']
        rsMember = Member.objects.get(member_no=memberno)

        context['member_no'] = rsMember.member_no
        context['member_id'] = rsMember.member_id
        context['member_name'] = rsMember.member_name
        context['member_email'] = rsMember.member_email

        context['flag'] = '0'
        context['result_msg'] = '회원 정보가 없습니다.'

        return render(request, "member_edit.html", context)

    else:
        context['flag'] = '1'
        context['result_msg'] = '회원 정보가 없습니다.'

        return redirect('/')


@csrf_exempt
def member_update(request):
    context = {}

    membername = request.GET['member_name']
    memberemail = request.GET['member_email']

    if 'member_no' in request.session:
        memberno = request.session['member_no']
        rsMember = Member.objects.get(member_no=memberno)

        rsMember.member_name = membername
        rsMember.member_email = memberemail
        rsMember.save()

        context['flag'] = '0'
        context['result_msg'] = '정보 변경되었습니다'

        return JsonResponse(context, content_type="application/json")

    else:
        context['flag'] = '1'
        context['result_msg'] = '회원 정보가 없습니다.'

        return JsonResponse(context, content_type="application/json")
