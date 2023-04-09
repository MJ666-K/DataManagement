from django.shortcuts import render, redirect
from DepartUserPretty import models
from DepartUserPretty.DPUModelForm import PrettyModelForm, PrettyEditModelForm
from DepartUserPretty.utils.pagination import Paginstion
# Create your views here.


def pretty_list(request):
    """靓号列表 + 搜索靓号"""
    date_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        date_dict["mobile__contains"] = search_data
    queryset = models.PrettyNum.objects.filter(**date_dict).order_by("-level")
    page_object = Paginstion(request, queryset)
    context = {
        'queryset': page_object.page_queryset,  # 分完页的数据
        "search_data": search_data,
        "page_string": page_object.html(), # 页码
    }
    return render(request, "pretty_list.html", context)


def pretty_add(request):
    """增加靓号"""
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "pretty_add.html", {"form": form})


def pretty_delete(request, nid):
    """ 删除靓号 """
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")


def pretty_edit(request, nid):
    """ 靓号编辑 """
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        return render(request, "pretty_edit.html", {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "pretty_add.html", {"form": form})


