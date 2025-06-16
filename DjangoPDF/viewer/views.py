from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
import fitz  # PyMuPDF
import os
import requests
from io import BytesIO

def get_pdf_file_object_from_url(pdf_url):
    response = requests.get(pdf_url)
    if response.status_code == 200:
        pdf_file = BytesIO(response.content)
        return pdf_file
    else:
        raise Exception(f"Failed to download PDF: {response.status_code}")

def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf_file = request.FILES['pdf']
        pdf_path = default_storage.save('uploaded.pdf', pdf_file)
        doc = fitz.open(default_storage.path(pdf_path))

        image_paths = []
        output_dir = os.path.join('viewer', 'static', 'images')
        os.makedirs(output_dir, exist_ok=True)

        # 기존 이미지 삭제
        for f in os.listdir(output_dir):
            if f.startswith("page_"):
                os.remove(os.path.join(output_dir, f))

        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=150)
            img_name = f'page_{i + 1}.png'
            full_path = os.path.join(output_dir, img_name)
            pix.save(full_path)
            image_paths.append(f'/static/images/{img_name}')

        request.session['image_paths'] = image_paths
        return redirect('/view/?page=0')

    return render(request, 'viewer/upload.html')


# def view_pages(request):
#     images = request.session.get('image_paths', [])
#     page = int(request.GET.get('page', 0))
#     total_pairs = (len(images) + 1) // 2
#
#     start = page * 2
#     end = start + 2
#     current_pair = images[start:end]
#
#     context = {
#         'pages': current_pair,
#         'has_prev': page > 0,
#         'has_next': page + 1 < total_pairs,
#         'prev_page': page - 1,
#         'next_page': page + 1,
#     }
#
#     return render(request, 'viewer/viewer.html', context)

# def view_pages(request):
#     images = request.session.get('image_paths', [])
#     page = int(request.GET.get('page', 0))
#     total_pairs = (len(images) + 1) // 2
#
#     start = page * 2
#     end = start + 2
#     current_pair = images[start:end]
#
#     # 페이지 번호와 이미지 페어로 묶기
#     pages_with_numbers = []
#     for i, img in enumerate(current_pair):
#         page_number = start + i + 1  # 페이지는 1부터 시작
#         pages_with_numbers.append((img, page_number))
#
#     context = {
#         'pages': pages_with_numbers,
#         'has_prev': page > 0,
#         'has_next': page + 1 < total_pairs,
#         'prev_page': page - 1,
#         'next_page': page + 1,
#     }
#
#     return render(request, 'viewer/viewer.html', context)

# def view_pages(request):
#     images = request.session.get('image_paths', [])
#     page = int(request.GET.get('page', 0))
#     total_pages = len(images)
#     total_pairs = (total_pages + 1) // 2
#
#     start = page * 2
#     end = start + 2
#     current_pair = images[start:end]
#
#     pages_with_numbers = []
#     for i, img in enumerate(current_pair):
#         page_number = start + i + 1  # 실제 페이지 번호 (1부터 시작)
#         pages_with_numbers.append((img, page_number))
#
#     context = {
#         'pages': pages_with_numbers,
#         'total_pages': total_pages,
#         'has_prev': page > 0,
#         'has_next': page + 1 < total_pairs,
#         'prev_page': page - 1,
#         'next_page': page + 1,
#     }
#
#     return render(request, 'viewer/viewer.html', context)

def view_pages(request):
    images = request.session.get('image_paths', [])
    page = int(request.GET.get('page', 0))
    total_pages = len(images)
    total_pairs = (total_pages + 1) // 2

    start = page * 2
    end = start + 2
    current_pair = images[start:end]

    pages_with_numbers = []
    for i, img in enumerate(current_pair):
        page_number = start + i + 1  # 실제 페이지 번호 (1부터 시작)
        pages_with_numbers.append((img, page_number))

    # 시작–끝 페이지 범위
    page_range = (start + 1, min(end, total_pages))

    context = {
        'pages': pages_with_numbers,
        'total_pages': total_pages,
        'page_range': page_range,
        'has_prev': page > 0,
        'has_next': page + 1 < total_pairs,
        'prev_page': page - 1,
        'next_page': page + 1,
    }

    return render(request, 'viewer/viewer.html', context)

def view_pages2(request):
    context = {}

    return render(request, 'viewer/viewer2.html', context)