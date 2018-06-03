# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from post.models import *


class postAdmin(admin.ModelAdmin):
    ''' 显示管理后台时的显示字段'''
    list_display = ["title","created"]

admin.site.register(Post,postAdmin)
admin.site.register(Tag)
admin.site.register(Category)