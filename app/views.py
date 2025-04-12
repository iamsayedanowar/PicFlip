from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from .utils import img_convert
import os

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES.get('file'):
        input_file = request.FILES['file']
        output_format = request.POST.get('format')
        fs = FileSystemStorage()
        filename = fs.save(input_file.name, input_file)
        uploaded_file_path = fs.path(filename)
        try:
            output_path = img_convert(uploaded_file_path, output_format)
            return FileResponse(open(output_path, 'rb'), as_attachment=True)
        except Exception as e:
            return render(request, 'index.html', {'error': str(e)})
    return render(request, 'index.html')

# Production Code

# def index(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         input_file = request.FILES['file']
#         output_format = request.POST.get('format')
#         tmp_media_root = '/tmp/media'
#         os.makedirs(tmp_media_root, exist_ok=True)
#         fs = FileSystemStorage(location=tmp_media_root)
#         filename = fs.save(input_file.name, input_file)
#         uploaded_file_path = fs.path(filename)
#         try:
#             output_path = img_convert(uploaded_file_path, output_format)
#             response = FileResponse(open(output_path, 'rb'), as_attachment=True)
#             def cleanup():
#                 try:
#                     os.remove(uploaded_file_path)
#                     os.remove(output_path)
#                 except Exception:
#                     pass
#             cleanup()
#             return response
#         except Exception as e:
#             return render(request, 'index.html', {'error': str(e)})
#     return render(request, 'index.html')