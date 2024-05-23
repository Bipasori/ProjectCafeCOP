import os
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from datetime import datetime

from .models import CHSource

from PIL import Image
import pytesseract

# 실행파일 위치지정
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def home(request):
    context = {}
    context['menutitle'] = 'Home'

    rsSource = CHSource.objects.filter(usage_flag='1').order_by('-id')
    context['rsSource'] = rsSource

    return render(request, 'home.html', context)


def coocr_upload(request):
    context = {}

    resulttext = ''
    imgname = ''
    if 'uploadfile' in request.FILES:
        uploadfile = request.FILES.get('uploadfile', '')

        fsize1 = uploadfile.size
        print(fsize1)

        currenttime = datetime.now()

        if uploadfile != '':

            name_old = uploadfile.name
            name_ext = os.path.splitext(name_old)[1]

            if name_ext == '.png' or name_ext == '.jpg' or name_ext == '.gif':

                fs = FileSystemStorage(location='static/source')
                imgname = fs.save(f"src-{name_old}", uploadfile)

                imgfile = Image.open(f"./static/source/{imgname}")

                resulttext = pytesseract.image_to_string(imgfile, lang='kor')

                rsSource = CHSource.objects.create(src_file=name_old,
                                                   src_name=f'{imgname}',
                                                   src_link=f'src-{name_old}',
                                                   result_text=resulttext,
                                                   created_at=datetime.now(),
                                                   )

            else:
                print(f"{name_ext} .png .jpg .gif 만 가능합니다.")

    context['resulttext'] = resulttext
    context['imgname'] = imgname

    return render(request, "coocr_upload.html", context)
