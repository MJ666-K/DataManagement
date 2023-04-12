$(function () {
    initBar();
    initPie();
    initLine();
})

/**
 * 初始化柱状图
 */
function initBar() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m2'));

    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '员工业绩阅读汇总信息',
            // subtext: 'MJ公司',
            textAlign: 'auto',
            left: 'center',
        },
        tooltip: {},
        legend: {
            data: [],
            bottom: 0,
        },
        xAxis: {
            data: []
        },
        yAxis: {},
        series: []
    };

    $.ajax({
        url: '/chart/bar/',
        type: 'get',
        dataType: 'JSON',
        success: function (res) {
            // 将后台返回的数据，更新到option中
            if (res.status) {
                option.legend.data = res.data.legend;
                option.xAxis.data = res.data.x_axis;
                option.series = res.data.series_list;
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
            }
        }
    })
}

/**
 * 初始化饼状图
 */
function initPie() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m3'));
    var option = {
        title: {
            text: '部门预算占比',
            subtext: 'MJ分公司',
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            bottom: 0,
        },
        series: [
            {
                name: '预算',
                type: 'pie',
                radius: '50%',
                data: [],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    $.ajax({
        url: '/chart/pie/',
        type: 'get',
        dataType: 'JSON',
        success: function (res) {
            if (res.status) {
                option.series[0].data = res.data;
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
            }
        }
    })
}

/**
 * 初始化折线图
 */
function initLine() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m1'));
    var option = {
        title: {
            text: 'MJ666-K Company',
            left: 'center'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: [],
            bottom: 0,
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: []
    };

    $.ajax({
        url: '/chart/line/',
        type: 'get',
        dataType: 'JSON',
        success: function (res) {
            if (res.status) {
                option.legend.data = res.data.legend;
                option.xAxis.data = res.data.x_axis;
                option.series = res.data.series_list;
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
            }
        }
    })
}