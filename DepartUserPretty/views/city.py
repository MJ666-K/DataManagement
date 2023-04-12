from django.shortcuts import render, redirect
from DepartUserPretty import models
from DepartUserPretty.PublicModelForm import UpModelForm


def city_list(request):
    queryset = models.City.objects.all()

    return render(request, "city_list.html", {"queryset": queryset})


def city_add(request):
    """添加城市"""
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, "upload.html", {"form": form, "title": "添加城市"})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/city/list/")
    return render(request, "upload.html", {"form": form, "title": "添加城市"})