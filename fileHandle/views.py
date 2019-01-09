from django.shortcuts import render,HttpResponse,redirect
import json
import os
# Create your views here.


def uploadFile(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        with open(os.path.join('uploadFileDemo', my_file.name), 'wb') as f:
            for line in my_file.chunks():
                f.write(line)
        return HttpResponse('上传成功')
    return render(request,'upload.html')

def readFile(request):
    if request.method == 'GET':
        with open(os.path.join('uploadFileDemo', 'testfile.txt')) as f:
            data = f.read()
        return render(request,'readfile.html',locals())