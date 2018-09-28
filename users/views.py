from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户,注册用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)      # 用提交表单中的数据创建用户

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])       # 使用创建用户时输入两次中的随便一个密码，这里获取与键'password1'相关联的值
            login(request, authenticated_user)      # 为新用户创建有效的会话
            return HttpResponseRedirect(reverse('learning_logs:index'))         # 将用户重定向到主页
    context = {'form': form}
    return render(request, 'users/register.html', context)











