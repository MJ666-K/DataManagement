from django import forms
from DepartUserPretty import models
from django.core.exceptions import ValidationError
from DepartUserPretty.utils.BootstrapModelform import BootStrapModelForm


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
