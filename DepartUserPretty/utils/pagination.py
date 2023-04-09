"""自定义分页组件
使用方法：
视图函数：
def pretty_list(request):
    # 1.根据自己的需求筛选数据
    queryset = models.PrettyNum.objects.filter()
    # 2.实例化分页对象
    page_object = Paginstion(request, queryset)
    context = {
        'queryset': page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(), # 页码
    }
    return render(request, "pretty_list.html", context)

HTML页面中：
        {% for obj in queryset %}
            {{ obj.xx}}
        {% endfor %}

        <ul class="pagination">
            {{ page_string }}
        </ul>

"""
from django.utils.safestring import mark_safe
from django.http.request import QueryDict
import copy


class Paginstion(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 显示分页器显示当前页的前5个和后5个
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库数据较少，没有达到11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库的数据较多，大于11页
            # 当前页小于5
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页 > 5 and 当前页 + 5 > 总页码
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}"><span aria-hidden="true">«</span></a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}"><span aria-hidden="true">«</span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}"><span aria-hidden="true">»</span></a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}"><span aria-hidden="true">»</span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))
        search_string = """
            <li>
                <form method="get" style="float: left; margin-left: -1px">
                    <input name="page"
                            style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0;"
                            type="text" class="form-control" placeholder="页 码">
                    <button style="border-radius: 0" class="btn btn-default" type="submit">跳 转</button>
                </form>
            </li>
            """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string


