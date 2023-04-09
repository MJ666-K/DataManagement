
# Employee Management System

基于`python3.10和`Django4.1`的部门人员数据管理

## 环境安装

mysql客户端从`pymysql`修改成了`mysqlclient`，具体请参考 [pypi](https://pypi.org/project/mysqlclient/) 查看安装前的准备。

使用pip安装： `pip install mysqlclient`

如果你没有pip，使用如下方式安装：

- OS X / Linux 电脑，终端下执行:

  ```python
  curl http://peak.telecommunity.com/dist/ez_setup.py | python
  curl https://bootstrap.pypa.io/get-pip.py | python
  ```

- Windows电脑：

  下载 http://peak.telecommunity.com/dist/ez_setup.py 和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py 这两个文件，双击运行。

## 运行

修改`EMSystem/setting.py` 修改数据库配置，如下所示：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manage',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 3306,
    }
}
```

### 创建数据库

mysql数据库中执行:

```mysql
CREATE DATABASE `manage` ;
```

然后终端下执行:

```python
python manage.py makemigrations
python manage.py migrate
```

### 开始运行：

执行： `python manage.py runserver`

浏览器打开: http://127.0.0.1:8000/ 就可以看到效果了。

## 问题相关
有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 `2212013739@qq.com`.我会尽快解答.推荐提交Issue方式.
