# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(verbose_name=u'이름', max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'분류'
        ordering=['name']


class Item(models.Model):
    M_TYPE = (
        ('JH', 'Medicine'),
        ('MJ', 'Life'),
        )

    mtype = models.CharField(max_length=10, choices=M_TYPE)
    category = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(max_length=256)
    picture = models.ImageField(upload_to="item_images", blank=True)
    text = models.TextField()
    # 이 user 를 foreignkey 로 해서 하는 방법을 강구해보자
    user = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'생성일')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'수정일')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u'글'
        ordering = ['created']


class Comment(models.Model):
    item = models.ForeignKey(Item, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['created']
