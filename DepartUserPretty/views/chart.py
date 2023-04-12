from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    """数据统计页面"""
    return render(request, "chart_list.html")


def chart_bar(request):
    """构造柱状图的数据"""
    legend = ['上海', '苏州']
    series_list = [
                    {
                        'name': '上海',
                        'type': 'bar',
                        'data': [5, 20, 36, 10, 10, 20, 90]
                    },
                    {
                        'name': '苏州',
                        'type': 'bar',
                        'data': [50, 25, 10, 45, 60, 90, 89]
                    },
                ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """构造饼图的数据"""
    db_data_list = [
                    {'value': 1048, 'name': 'IT部门'},
                    {'value': 735, 'name': '新媒体'},
                    {'value': 580, 'name': '运营'},
                    {'value': 484, 'name': '产品部'},
                    {'value': 300, 'name': '设备部'},
                ]
    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def chart_line(request):
    """构造折线图"""
    legend = ['上海', '苏州']
    series_list = [
        {
            'name': '上海',
            'type': 'line',
            'stack': 'Total',
            'data': [50, 25, 10, 45, 60, 90, 50]
        },
        {
            'name': '苏州',
            'type': 'line',
            'stack': 'Total',
            'data': [5, 20, 36, 10, 10, 20, 40]
        },
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,

        }
    }
    return JsonResponse(result)