from django.shortcuts import render
from album.models import Album
from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage
import datetime
import random
import sys, os

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

def album(request):
    rsAlbum = Album.objects.all().filter(a_usage='1')

    return render(request, "album_list.html", {
        'rsAlbum': rsAlbum
    })

def album_write(request):
    return render(request, "album_write.html", )

def album_insert(request):

    atitle = request.POST['a_title']
    atype = request.POST['a_type']
    anote = request.POST['a_note']

    name_date = str(datetime.datetime.today().year) + '_' + str(datetime.datetime.today().month) + '_' + str(datetime.datetime.today().day)

    uploaded_file = request.FILES['ufile']
    name_old = uploaded_file.name
    name_ext = os.path.splitext(name_old)[1]
    name_new = 'A' + name_date + '_' + str(random.randint(1000000000, 9999999999))

    fs = FileSystemStorage(location='static/board/photos')

    name = fs.save(name_new + name_ext, uploaded_file)

    rows = Album.objects.create(a_title=atitle, a_note=anote, a_type=atype, a_image=name, a_usage='1')

    return redirect('/album')


def album_view(request):
    ano = request.GET['a_no']

    rsData = Album.objects.get(a_no=ano)
    rsData.a_count += 1
    rsData.save()

    rsDetail = Album.objects.filter(a_no=ano)

    return render(request, "album_view.html", {
        'rsDetail': rsDetail,
        'a_no': ano,
    })

def album_edit(request):
    ano = request.GET['a_no']
    rsDetail = Album.objects.filter(a_no=ano)

    return render(request, "album_edit.html", {
        'rsDetail': rsDetail,
        'a_no': ano,
    })


def album_update(request):

    ano = request.POST['a_no']
    atitle = request.POST['a_title']
    atype = request.POST['a_type']
    anote = request.POST['a_note']

    if 'ufile' in request.FILES:
        name_date = str(datetime.datetime.today().year) + '_' + str(datetime.datetime.today().month) + '_' + str(datetime.datetime.today().day)

        uploaded_file = request.FILES['ufile']
        name_old = uploaded_file.name
        name_ext = os.path.splitext(name_old)[1]
        name_new = 'A' + name_date + '_' + str(random.randint(1000000000, 9999999999))

        fs = FileSystemStorage(location='static/board/photos')

        fname = fs.save(name_new + name_ext, uploaded_file)

        album = Album.objects.get(a_no=ano)
        album.a_title = atitle
        album.a_type = atype
        album.a_note = anote
        album.a_image = fname
        album.save()
    else:
        album = Album.objects.get(a_no=ano)
        album.a_title = atitle
        album.a_type = atype
        album.a_note = anote
        album.save()

    return redirect('/album')

def album_delete(request):
    ano = request.GET['a_no']
    album = Album.objects.get(a_no=ano)
    album.a_usage = '0'
    album.save()

    return redirect('/album')
