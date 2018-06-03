# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    ''' 创建分类的模型表,包含类别名称'''
    cname = models.CharField(max_length=30,verbose_name="类别")

    def __unicode__(self):
        return r"类别:%s"% self.cname

class Tag(models.Model):
    '''创建标签表,包含标签名称'''
    tname = models.CharField(max_length=30,verbose_name="标签")

    def __unicode__(self):
        return r"标签:%s"% self.tname

class Post(models.Model):
    '''帖子数据表,包含title,desc,content,created,modify,category(foreign),tag(many)字段'''
    title = models.CharField(max_length=30,verbose_name="标题")
    desc = models.TextField(verbose_name="摘要")
    content = RichTextUploadingField(verbose_name="正文")
    created = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    modify = models.DateTimeField(auto_now= True)
    category = models.ForeignKey(Category,verbose_name="类别")
    tag = models.ManyToManyField(Tag,verbose_name="标签")

    def __unicode__(self):
        return r"主题:%s"% self.title