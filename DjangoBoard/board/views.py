from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect

from django.db import connection

import pymysql

# # SQL Alchemy part
# from sqlalchemy import create_engine, select
# DB_URL = 'mysql+mysqldb://root:intra165@ㅣlocalhost:3306/edudb?charset=utf8'
# engine = create_engine(DB_URL)
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker()
# sess = Session()

def home(request):
    return render(request, "home.html")

def board(request):
    rsBoard = Board.objects.all()
    # print(rsBoard)

    return render(request, "board_list.html", {
        'rsBoard': rsBoard
    })

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


def ds_querytolist(request):

    rsBoard = Board.objects.all()

    print("Type of model query result : ")
    print(type(rsBoard))

    rsList = []

    for record in rsBoard:
        lst = list(record.b_title)
        rsList.append(lst)

    print("Type of list : ")
    print(type(rsList))
    print(rsList)

    return render(request, "datastudy.html", {})

def ds_orm(request):
    # CASE1 :
    rsBoard = Board.objects.all()
    print(type(rsBoard))

    # CASE2 :
    rsBoard2 = Board.objects.raw('SELECT * FROM board')
    print(type(rsBoard2))

    # CASE3 :
    with connection.cursor() as cursor0:
        cursor0.execute('SELECT * FROM board')
        rsBoard3 = cursor0.fetchall()
        cursor0.close

    print(type(rsBoard3))


    # CASE4 :
    dbCon = pymysql.connect('localhost', 'root', 'intra165', 'edudb')
    cursor1 = dbCon.cursor()
    cursor1.execute('SELECT * FROM board')
    rsBoard4 = cursor1.fetchall()
    cursor1.close

    print(type(rsBoard4))


    return render(request, "ds_orm.html", {
        'rsBoard': rsBoard,
        'rsBoard2': rsBoard2,
        'rsBoard3': rsBoard3,
        'rsBoard4': rsBoard4,
    })


def markdown2(request):
    return render(request, "markdown2.html")
