import sys
sys.path.append(r'D:\Graduation Design\Project\DiffusionModel\latent_diffuison')
from DiffusionModel.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login,logout
from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
from .models import User
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method ==  'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error_message': "账号不存在"})
        if username and password:
            username = username.strip()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # 将用户标记为已登录状态
                return redirect('/gen/')
            else:
                 return render(request, 'login.html', {'error_message' : "密码不正确"})  # 重定向到登录页面

    return  render(request , 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return render(request, 'register.html', {'error_message': "输入密码不一致"})
        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {'error_message': "用户已存在"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            return redirect('/login/')
    return render(request, 'register.html')

from DiffusionModel.latent_diffuison.scripts.txt2img import django_ldm
from django.contrib.auth.decorators import login_required

@login_required
def gen(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect("/login/")
    if request.method == "GET":
        return render(request, 'gen.html', {'user': user})
    #生成图片
    elif request.method == 'POST':
        text = request.POST.get('text_input', '')
        dldm = django_ldm(text)
        image_path = dldm.gen_picture()
        print(image_path)
        image_path_res = '/static/image/samples/'+str(text)
        dir = []
        for i in range(4):
            dir_i = image_path_res + f"000{i}.png"
            dir.append(dir_i)

        return render(request, 'gen.html', {'image_p': dir})
    return render(request, 'login.html')

from .models import User
def show_data(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_logout(request):
    logout(request)  # 使用 logout() 函数退出用户身份验证
    return redirect('/login')