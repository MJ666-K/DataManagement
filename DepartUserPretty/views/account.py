from django.shortcuts import render, redirect, HttpResponse
from DepartUserPretty.PublicModelForm import LoginForm
from DepartUserPretty import models
from DepartUserPretty.utils.code import check_code
from io import BytesIO


def login(request):
    """登录"""
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        print(user_input_code, "-", code)
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, "login.html", {"form": form})
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", {"form": form})
        request.session["info"] = {"id": admin_object.id, "name": admin_object.username}
        request.session.set_expiry(60*60*24*7)   # session保存7天
        return redirect("/admin/list/")
    return render(request, "login.html", {"form": form})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    """图片验证码"""
    img, code_string = check_code()
    request.session['image_code'] = code_string
    request.session.set_expiry(60)  # 设置60秒超时
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())

