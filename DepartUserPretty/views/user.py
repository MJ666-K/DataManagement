from django.shortcuts import render, redirect
from DepartUserPretty import models
from DepartUserPretty.PublicModelForm import UserModelForm
from DepartUserPretty.utils.pagination import Paginstion
# Create your views here.


def user_list(request):
    """ 用户列表 """
    date_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        date_dict["name__contains"] = search_data
    queryset = models.UserInfo.objects.filter(**date_dict)
    page_object = Paginstion(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data,
    }
    return render(request, 'user_list.html', context)


def user_add(request):
    """ 添加用户"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, "user_add.html", {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_add.html", {"form": form})


def user_delete(request, nid):
    """ 删除用户 """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')


def user_edit(request, nid):
    """ 编辑用户 """
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})

