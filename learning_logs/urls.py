#_*_ coding:utf-8 _*_
"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

#from django.urls import path
app_name = 'learning_logs'      # 声明应用程序名称，否则runserver时报错
urlpatterns = [
    # 主页
    url('^$', views.index, name='index'),
    # 显示所有的主题
    url('^topics/$', views.topics, name='topics'),          # base.html中的learning_logs:topics 是匹配此处的'topics'中的URL模式匹配
    # 特定主题的详细页面
    url('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    url('^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    url('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]


