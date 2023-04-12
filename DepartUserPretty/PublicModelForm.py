from django import forms
from DepartUserPretty import models
from django.core.exceptions import ValidationError
from DepartUserPretty.utils.BootstrapModelform import BootStrapModelForm, BootStrapForm
from DepartUserPretty.utils.encrypt import md5


class LoginForm(BootStrapForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput, required=True)
    password = forms.CharField(label="密码",  widget=forms.PasswordInput(render_value=True), required=True)
    code = forms.CharField(label="验证码",  widget=forms.TextInput, required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


class AdminModelForm(BootStrapModelForm):
    conform_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["username", "password", "conform_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_conform_password(self):
        pwd = self.cleaned_data.get("password")
        conform = md5(self.cleaned_data.get("conform_password"))
        if conform != pwd:
            raise ValidationError("密码不一致！")
        return conform


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username"]


class AdminResetModelForm(BootStrapModelForm):
    conform_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["password", "conform_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('不能与以前的密码一致')
        return md5_pwd

    def clean_conform_password(self):
        pwd = self.cleaned_data.get("password")
        conform = md5(self.cleaned_data.get("conform_password"))
        if conform != pwd:
            raise ValidationError("密码不一致！")
        return conform


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "gender", "account", "create_time", "depart"]


class PrettyModelForm(BootStrapModelForm):
    # 验证：方式1
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')]
    # )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]
        # fields = "__all__"
        # exclude = ["level"]

    # 验证：方式2
    def clean_mobile(self):  # 钩子函数
        txt_mobile = self.cleaned_data["mobile"]  # 用户传入的数据
        if len(txt_mobile) != 11:
            raise ValidationError("手机号格式错误！")
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在！")
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="手机号")  # 使手机号不能编辑

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]  # 用户传入的数据
        if len(txt_mobile) != 11:
            raise ValidationError("手机号格式错误！")
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exclude(id=self.instance.pk).exists()
        if exists:
            raise ValidationError("手机号已存在！")
        return txt_mobile


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput  # Textarea
        }


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"
        exclude = ["oid", "admin"]


class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ["img"]
    name = forms.CharField(label="姓名")
    age = forms.CharField(label="年龄")
    img = forms.FileField(label="头像")


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]

    class Meta:
        model = models.City
        fields = "__all__"
