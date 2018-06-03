# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from post.models import Post

def getPostByPage(num):
    num = int(num)
    paginator = Paginator(Post.objects.order_by("-created"),per_page=1)

    #paginator.num_pages  根据提供的需要分页总量和每页页数计算的一共可以分的页数
    #越界规避
    if num < 1:
        num = 1
    elif num > paginator.num_pages:
        num = paginator.num_pages

    #计算每一页导航栏的初始页码和结束页码
    start = ((num - 1) / 10) * 10 + 1
    end = start + 10

    if end > paginator.num_pages:
        end = paginator.num_pages

    return paginator.page(num), range(start, end+1)
    #paginator.page(num) 获取页码为num的页面对象集合


def index_view(request,num=1):
    pagePost,PageRange = getPostByPage(num)

    return render(request,"index.html",{"posts":pagePost,"pagerange":PageRange})


def detials_view(request,post_id):
    post = Post.objects.get(id = post_id)

    return render(request,"detials.html",{"post":post})


def indexByCategory_view(request,categoryId):
    postbyCa = Post.objects.filter(category_id = categoryId)
    return render(request,"category.html",{"postbyCa":postbyCa})


def indexByDate_view(request,year,month):
    postby = Post.objects.filter(created__year=year,created__month=month)
    return render(request,"category.html",{"postbyCa":postby})


def postall(request):
    postall = Post.objects.order_by("-created")
    return render(request,"category.html",{"postbyCa":postall})


# 全文搜索功能
def search_view(request):
    from haystack.query import SearchQuerySet
    from haystack.query import SQ

    # 获取请求参数
    kws = request.GET.get('q','')
    search_posts = SearchQuerySet().filter(SQ(title=kws)|SQ(content=kws)|SQ(desc=kws))
    s_posts = []
    for s_p in search_posts:
        s_posts.append(s_p.object)
    return render(request,'category.html',{'postbyCa':s_posts})