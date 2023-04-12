var DELETE_ID;
var EDIT_ID;
$(function () {
    bindBtnAddEvent();
    bindBtnSaveEvent();
    bindBtnDeleteEvent();
    bindBtnbtnConfromDeleteEvent();
    bindBtnEditEvent();
})

function bindBtnAddEvent() {
    $('#btnAdd').click(function () {
        EDIT_ID = undefined;
        // 清空对话框中的数据
        $('#formAdd')[0].reset();
        $("#myModalLabel").text("新建")
        //点击新建按钮显示对话框
        $('#myModal').modal('show');
    });
}

function bindBtnSaveEvent() {
    $('#btnSave').click(function () {
        // 点击保存按钮
        // 清除错误信息
        $(".error-msg").empty();
        if (EDIT_ID) {
            // 编辑
            doEdit();
        } else {
            // 添加
            doAdd();
        }
    });
}

function doAdd() {
    // 向后台发送请求
    $.ajax({
        url: "/order/add/",
        type: "post",
        data: $("#formAdd").serialize(),
        dataType: "JSON",
        success: function (res) {
            if (res.status) {
                alert("创建成功");
                // 清空表单
                $("#formAdd")[0].reset();
                // 关闭对话框
                $("#myModal").modal("hide");
                location.reload();
            } else {
                $.each(res.error, function (name, errorList) {
                    $("#id_" + name).next().text(errorList[0])
                })
            }
        }
    })
}

function doEdit() {
    // 向后台发送请求
    $.ajax({
        url: "/order/SaveEdit/?uid=" + EDIT_ID,
        type: "post",
        data: $("#formAdd").serialize(),
        dataType: "JSON",
        success: function (res) {
            if (res.status) {
                alert("创建成功");
                // 清空表单
                $("#formAdd")[0].reset();
                // 关闭对话框
                $("#myModal").modal("hide");
                location.reload();
            } else {
                if (res.tips) {
                    alert(res.tips);
                } else {
                    $.each(res.error, function (name, errorList) {
                        $("#id_" + name).next().text(errorList[0])
                    })
                }
            }
        }
    })
}

function bindBtnDeleteEvent() {
    $('.btn-delete').click(function () {
        // alert("点击了删除！");
        $("#deleteModal").modal('show');
        // 获取当前行的ID
        DELETE_ID = $(this).attr("uid");

    });
}

function bindBtnbtnConfromDeleteEvent() {
    $('#btnConfromDelete').click(function () {
        // 点击确认删除按钮
        $.ajax({
            url: "/order/delete/",
            type: "GET",
            data: {
                uid: DELETE_ID
            },
            dataType: "JSON",
            success: function (res) {
                if (res.status) {
                    // alert("删除成功")
                    // 隐藏删除框
                    // $("#deleteModal").modal('hide');
                    // DELETE_ID = 0;
                    location.reload();
                } else {
                    // 删除失败
                    alert((res.error));
                }
            }
        });
    });
}

function bindBtnEditEvent() {
    $(".btn-edit").click(function () {
        // 清空对话框中的数据
        $('#formAdd')[0].reset();
        var uid = $(this).attr("uid");
        EDIT_ID = uid;
        // 发送ajax去后台获取当前行的相关数据  /order/edit/?uid=123
        $.ajax({
            url: "/order/edit/",
            type: 'get',
            data: {
                uid: uid
            },
            dataType: "JSON",
            success: function (res) {
                if (res.status) {
                    // 将数据默认赋值到对话框的标签
                    $.each(res.data, function (name, value) {
                        $("#id_" + name).val(value);
                    })
                    // 修改对话框的标题
                    $("#myModalLabel").text("编辑");
                    // 点击编辑，显示对话框
                    $('#myModal').modal('show');

                } else {
                    alert(res.error);
                }
            }
        })
        // 在对话框中默认看到
    });
}