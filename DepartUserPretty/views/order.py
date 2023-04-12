import json
import random
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from DepartUserPretty import models
from DepartUserPretty.PublicModelForm import OrderModelForm
from DepartUserPretty.utils.pagination import Paginstion
# Create your views here.


def order_list(request):
    """订单列表"""
    queryset = models.Order.objects.all().order_by('-id')
    page_object = Paginstion(request, queryset)
    form = OrderModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, "order_list.html", context)


@csrf_exempt
def order_add(request):
    """新建订单（Ajax请求）"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        form.instance.admin_id = request.session['info']['id']
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


def order_delete(request):
    """删除订单"""
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在！"})
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_edit(request):
    """编辑订单"""
    nid = request.GET.get("uid")
    row_dict = models.Order.objects.filter(id=nid).values("title", "price", "status").first()
    if not row_dict:
        return JsonResponse({"status": False, "msg": "数据不存在！！！"})
    context = {
        "status": True,
        "data": row_dict,
    }
    return JsonResponse(context)


@csrf_exempt
def order_SaveEdit(request):
    """保存编辑订单"""
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在，请刷新重试！"})
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})

    return JsonResponse({"status": False, "error": form.errors})



