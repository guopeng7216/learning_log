# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic
from .forms import TopicForm
from .forms import TopicForm, EntryForm
from .models import Topic, Entry

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')      # request原始请求对象

@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')       # 数据库中获取主题数据,代码Topic.objects.filter(owner=request.user)让Django只从数据库中获取owner属性为当前用户的Topic对象。
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)        #此处context的字典下列表topics的内容传递到topics.html中

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户,
    if topic.owner != request.user:         # 如果请求的主题不归当前用户所有，我们就引发Http404异常
        raise Http404
    entries = topic.entry_set.order_by('-date_added')       # -date_added减号为降序
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)      # 用户输入的数据存在request.POST中
        if form.is_valid():                 # 自动检查提交信息是否有效，且输入的数据与要求的字段类型一致
            new_topic = form.save(commit=False)     # 传递实参commit=False，这是因为我们先修改新主题，再将其保存到数据库中
            new_topic.owner = request.user          # 将当前的用户设置为主题的属主
            new_topic.save()            # 将表单中的数据写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))            # 重定向网页到topics
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)     # 不将提交的条目保存到数据库中
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)      # 获取用户要修改的条目对象内容
    topic = entry.topic                         # 获取条目相关联的主题
    if topic.owner != request.user:             # 检查主题的所有者是否是当前登录的用户，如果不是，就引发Http404异常。
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)        # 这个实参让Django创建一个表单，并使用既有条目对象中的信息填充它。
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)     # 根据既有条目对象创建一个表单实例，并根据request.POST中的相关数据对其进行修改
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)







