from django.shortcuts import render, redirect
from DepartUserPretty import models
from DepartUserPretty.utils.pagination import Paginstion
from DepartUserPretty.PublicModelForm import AdminModelForm, AdminEditModelForm, AdminResetModelForm


def admin_list(request):
    """管理员列表 + 搜索"""
    date_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        date_dict["username__contains"] = search_data
    queryset = models.Admin.objects.filter(**date_dict)
    page_object = Paginstion(request, queryset)
    context = {
        'queryset': page_object.page_queryset,  # 分完页的数据
        "search_data": search_data,
        "page_string": page_object.html(),  # 页码
    }
    return render(request, "admin_list.html", context)


def admin_add(request):
    """添加管理员"""
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "Public.html", {"title": "新建管理员", "form": form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, "Public.html", {"title": "新建管理员", "form": form})


def admin_edit(request, nid):
    """编辑管理员"""
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, "Public.html", {"title": "编辑管理员", "form": form})
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'Public.html', {"title": "编辑管理员", "form": form})


def admin_delete(request, nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def admin_reset(request, nid):
    """重置密码"""
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    title = "重置密码 - {}".format(row_object)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'Public.html', {"title": title, "form": form})
    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'Public.html', {"title": title, "form": form})





