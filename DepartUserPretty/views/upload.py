import os
from django.shortcuts import render, HttpResponse, redirect
from DepartUserPretty import models
from DepartUserPretty.PublicModelForm import UpForm, UpModelForm
from django.conf import settings


def upload_document(request):
    """头像上传"""
    if request.method == 'GET':
        form = UpForm()
        return render(request, "upload.html", {"form": form, "title": "上传"})
    form =UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 读取图片内容写入到文件夹中，并获取文件路径
        image_object = form.cleaned_data.get("img")
        # media_path = os.path.join(settings.MEDIA_ROOT, image_object.name)  # 绝对路径
        media_path = os.path.join("media", image_object.name)  # 相对路径
        f = open(media_path, mode="wb")
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        # 将图片文件路径写入到数据库
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            img=media_path
        )
        return redirect("/upload/document/")
    return render(request, 'upload.html', {"form": form, "title": "上传"})