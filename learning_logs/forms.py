#_*_ coding:utf-8 _*_
from django import forms
from .models import Topic
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic           # 根据模型Topic创建一个表单
        fields = ['text']       # 该表单只包含字段text
        labels = {'text': ''}   # 让Django不要为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}      #定义文本区域，宽度设置为80列，默认为40列
