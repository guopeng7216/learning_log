# _*_ coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)         # CharField由字符或文本组成的数据,长度为200字符
    date_added = models.DateTimeField(auto_now_add=True)    # 创建新主题时，Django将这个属性自动设置成当前日期和时间。
    owner = models.ForeignKey(User, on_delete=models.CASCADE)          # 需加上on_delete=models.CASCADE，否则报错：TypeError: __init__() missing 1 required positional argument: 'on_delete'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."