from django.shortcuts import render, redirect
from DepartUserPretty import models
from DepartUserPretty.utils.pagination import Paginstion
# Create your views here.


def depart_list(request):
    """ 部门列表 """
    queryset = models.Department.objects.all()
    page_object = Paginstion(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, "depart_list.html", context)


def depart_add(request):
    """ 新建部门 """
    if request.method == 'GET':
        return render(request, "depart_add.html")
    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect('/depart/list/')


def depart_delete(request):
    """ 删除部门 """
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list')


def depart_edit(request, nid):
    """ 修改部门 """
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {'row_object': row_object})
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list')

