# Django项目步骤
## 新建项目
1. pycharm创建项目，指定文件夹
2. 删除setting.py中的TEMPLATES下的 'DIRS': [BASE_DIR / 'templates']
3. 删除templates文件夹

## 创建app
1. 找到pycharm上方Tools中的Run manage.py...
2. startapp <项目名称>
3. 找到settings.py中的INSTALLED_APPS，注册我们的项目名称： <项目名称>apps.<...>

## 设计表结构orm
1. 找到项目中的models.py，设计自己的表结构
```python
class UserInfo(models.Model):
    '''用户表'''
    name = models.CharField(verbose_name='账号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    #有约束 on_delete=models.CASCADE代表级联删除
    depart = models.Foreignkey(to='表名',to_field='表中的列',null=True,blank=True,on_delete=models.CASCADE)
```
## MySQL生成表
1. 启动mysql：mysql -u 用户名 -p
2. 输入密码 
3. 创建数据库 create database <数据库名字> 
4. 修改配置文件，链接mysql
- 在settings中设置DATABASES参数
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ceshi',
        'USER': 'root',
        'PASSWORD': 'yuanke.0825',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```
- 使用django命令生成数据库表
找到pycharm上方Tools中的Run manage.py...
输入makemigrations然后输入migrate

## 静态文件管理
1. 在项目目录下创建static文件夹，可以在文件夹下创建css，js，image，plugins等文件夹
2. 创建模板文件夹

## 前端项目流程
1. 在urls.py中配置网页地址和函数
```python
from DiffusionModel import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #登录
    path('login/', views.login),
    #注册
    path('register/', views.register),
    #生成界面
    path('gen/', views.gen),

]
```
2. 在views.py中写函数 
```python
def login(request):
    # 登录
    return render(request,'login.html')
```
3. 在templates文件夹中创建html文件
```html
{% load static %}

<!DOCTYPE html>
<html lang="zh-CN">
<head>
     <meta charset="UTF-8">
    <title>用户注册</title>
     <link rel="stylesheet" type="text/css" href="{% static 'css/login.css' %}">
</head>
<body>
    <div class="container">
        <h1>用户注册</h1>
        <form id="registration-form">
            <input type="text" id="username" placeholder="账号" required>
            <input type="password" id="password" placeholder="密码" required>
            <input type="number" id="age" placeholder="年龄" required>
            <button type="submit">注册</button>
        </form>
    </div>

    <script src="{% static "js/login.js" %}"></script>
</body>
</html>
```


