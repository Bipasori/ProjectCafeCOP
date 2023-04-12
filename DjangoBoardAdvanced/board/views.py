from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect
import requests
import json

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

def home(request):
    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        memberno = None
        membername = None

    context["member_no"] = memberno
    context["member_name"] = membername

    return render(request, "home.html", context)

def boardheroku(request):
    rsBoard = Board.objects.filter(usage_flag="1")
    # print(rsBoard)

    return render(request, "boardheroku.html", {
        'rsBoard': rsBoard
    })

def board(request):
    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        return redirect('/')

    context["member_no"] = memberno
    context["member_name"] = membername

    rsBoard = Board.objects.filter(usage_flag="1")

    context["rsBoard"] = rsBoard

    return render(request, "board_list.html", context)

def board_write(request):
    return render(request, "board_write.html", )

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')
    else:
        return redirect('/board_write')

def board_view(request):
    bno = request.GET['b_no']

    rsData = Board.objects.get(b_no=bno)
    rsData.b_count += 1
    rsData.save()

    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail
    })

def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {
        'rsDetail': rsDetail
    })


def board_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return Response({"success": False, "msg": "게시글 없음"})

def board_delete(request):
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/board')

def board_ajax(request):
    # rsBoard = Board.objects.all()
    # print(rsBoard)
    rsBoard = Board.objects.filter(usage_flag="1")[:3]

    return render(request, "board_ajax.html", {
        'rsBoard': rsBoard
    })


@csrf_exempt
def board_deleteajax(request):

    bno = request.GET['b_no']

    rsBoard = Board.objects.get(b_no=bno)
    rsBoard.usage_flag = "0"
    rsBoard.save()

    context = {}
    context['result_msg'] = 'Deleted...'
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def board_updatepost(request):
    context = {}

    if request.method == "POST":
        bodydata = request.body.decode('utf-8')
        bodyjson = json.loads(bodydata)
        bno = bodyjson['bno']
        bvalue = bodyjson['bvalue']

    rsBoard = Board.objects.get(b_no=bno)
    rsBoard.b_title = bvalue
    rsBoard.save()

    context['result_msg'] = 'Updated...'
    return JsonResponse(context, content_type="application/json")


#***************************************************************************************************
# API로 만드는 Board
# https://groups.google.com/forum/#!topic/django-rest-framework/VxDhLtkJwiU
#***************************************************************************************************

def boardapi(request):

    import pandas as pd

    query1 = """
        {
          BoardAll {
            bNo
            bTitle
            bWriter
            bNote
            bCount
            bDate
          }
        }
    """

    # print(query1)

    url = 'http://127.0.0.1:8000/graphql'
    result = requests.get(url, json={'query': query1})
    #print(type(result))

    json_data = json.loads(result.text)
    #print(type(json_data))

    df_data = json_data['data']['BoardAll']
    print(type(df_data))

    df = pd.DataFrame(df_data)
    df = df[df.columns[::-1]]
    #print(type(df))

    rsBoard = [tuple(r) for r in df.to_numpy()]
    #print(type(rsBoard))

    return render(request, "boardapi_list.html", {
        'rsBoard': rsBoard
    })


def boardapi_view(request):
    bno = request.GET['b_no']

    query1 = "{ BoardDetail(bNo:" + bno + ") {  bNo bTitle bWriter bNote bCount bDate } }"

    # print(query1)

    url = 'http://127.0.0.1:8000/graphql'
    result = requests.get(url, json={'query': query1})
    json_data = json.loads(result.text)
    rsDetail = json_data['data']['BoardDetail']

    return render(request, "boardapi_view.html", {
        'rsDetail': rsDetail
    })


def boardapi_write(request):
    return render(request, "boardapi_write.html", )


@csrf_exempt
def boardapi_insert(request):
    btitle = request.GET['b_title']
    bwriter = request.GET['b_writer']
    bnote = request.GET['b_note']

    query1 = 'mutation BoardCreate { boardCreate (bTitle: "' + btitle \
             + '", bWriter: "' + bwriter \
             + '", bNote: "' + bnote + '") {  board { bNo bTitle bWriter bNote bCount } } } '

    print(query1)

    url = 'http://127.0.0.1:8000/graphql'
    result = requests.post(url, json={'query': query1})

    json_data = json.loads(result.text)

    return redirect('boardapi')


def boardapi_edit(request):
    bno = request.GET['b_no']

    query1 = "{ BoardDetail(bNo:" + bno + ") {  bNo bTitle bWriter bNote bCount bDate } }"

    print(query1)

    url = 'http://127.0.0.1:8000/graphql'
    result = requests.get(url, json={'query': query1})
    json_data = json.loads(result.text)
    rsDetail = json_data['data']['BoardDetail']

    return render(request, "boardapi_edit.html", {
        'rsDetail': rsDetail
    })


@csrf_exempt
def boardapi_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bwriter = request.GET['b_writer']
    bnote = request.GET['b_note']

    query1 = 'mutation BoardUpdate { boardUpdate (bNo:' + str(bno) + 'bTitle: "' + btitle \
             + '", bWriter: "' + bwriter \
             + '", bNote: "' + bnote + '") {  board { bNo bTitle bWriter bNote bCount } } } '

    print(query1)

    url = 'http://127.0.0.1:8000/graphql'
    result = requests.post(url, json={'query': query1})

    json_data = json.loads(result.text)

    return redirect('boardapi')


@csrf_exempt
def boardapi_deleteajax(request):

    bno = request.GET['b_no']

    querydel = ' mutation BoardDelete { boardDelete(bNo: ' + str(bno) + ') { board { bTitle bWriter bNote } } }'

    url = 'http://127.0.0.1:8000/graphql'

    result = requests.post(url, json={'query': querydel})

    json_data = json.loads(result.text)

    context = {}
    context['result_msg'] = 'Board deleted...'

    return JsonResponse(context, content_type="application/json")


def portfolio(request):
    rsBoard = Board.objects.all()

    return render(request, "portfolio.html", {
        'rsBoard': rsBoard
    })

def portfolio_detail(request):
    rsBoard = Board.objects.all()
    return render(request, "portfolio_details.html", {
        'rsBoard': rsBoard
    })

