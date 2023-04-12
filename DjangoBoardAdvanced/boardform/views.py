from django.shortcuts import render
from django.shortcuts import redirect
import requests
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Boardnew, Boardtype

from .forms import BoardForm, RawBoardForm

def boardform(request):
    context = {}

    #rsBoard = Boardnew.objects.filter(usage_flag="1").order_by("-b_no")
    rsBoard = Boardnew.objects.filter(usage_flag="1").select_related("type")

    context["rsBoard"] = rsBoard

    return render(request, "boardform.html", context)


def boardform_create(request):
    initial_data = {
        'b_title':'Title here'
    }

    board_form = BoardForm(request.POST or None, initial=initial_data)

    if board_form.is_valid():
        board_form.save()
        board_form = BoardForm()
    else:
        print(board_form.errors)

    context = {}
    context["form"] = board_form

    return render(request, "boardform_write.html", context)

def boardform_update(request):

    bno = request.GET['bno']
    obj = Boardnew.objects.get(b_no=bno)
    board_form = BoardForm(request.POST or None, instance=obj)

    if board_form.is_valid():
        board_form.save()
        # board_form = BoardForm()
    else:
        print(board_form.errors)

    context = {}
    context["form"] = board_form

    return render(request, "boardform_write.html", context)

# def boardform_create(request):
#     board_form = BoardForm(request.POST or None)
#
#     if board_form.is_valid():
#         board_form.save()
#         board_form = BoardForm()
#     else:
#         print(board_form.errors)
#
#     context = {}
#     context["form"] = board_form
#
#     return render(request, "boardform_write.html", context)


# def boardform_create(request):
#     board_form = RawBoardForm()
#
#     if request.method == "POST":
#         board_form = RawBoardForm(request.POST)
#
#         if board_form.is_valid():
#             # board_form.save()
#             # board_form = BoardForm()
#             print(board_form.cleaned_data)
#             Boardnew.objects.create(**board_form.cleaned_data)
#         else:
#             print(board_form.errors)
#
#     context = {}
#     context["form"] = board_form
#
#     return render(request, "boardform_write.html", context)
