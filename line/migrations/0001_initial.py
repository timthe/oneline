# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='이름', max_length=50)),
            ],
            options={
                'verbose_name': '분류',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('user', models.CharField(null=True, max_length=256, blank=True)),
                ('created', models.DateTimeField(verbose_name='생성일', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='수정일', auto_now=True)),
                ('category', models.ForeignKey(null=True, blank=True, to='line.Category')),
            ],
            options={
                'verbose_name': '글',
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
    ]
