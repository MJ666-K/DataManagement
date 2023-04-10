from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """登录中间件"""
    def process_request(self, request):
        # request.path_info  # 获取当前用户请求的URL
        if request.path_info in ['/login/', '/image/code/']:
            return
        info_dict = request.session.get("info")
        if info_dict:
            return
        return redirect('/login/')