#_*_ coding:utf-8 _*_
"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
app_name = 'users'
urlpatterns = [
    # 登录页面,http://localhost:8000/users/login/匹配,单词users让Django在users/urls.py中查找，而单词login让它将请求发送给Django默认视图login
    url('^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    # 注销页面
    url('^logout/$', views.logout_view, name='logout'),
    # 注册页面，这个模式与URL http://localhost:8000/users/register/匹配，并将请求发送给我们即将编写的函数register()。
    url('^register/$', views.register, name='register'),
]
