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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='이름', max_length=50)),
            ],
            options={
                'verbose_name': '분류',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('mtype', models.CharField(max_length=10, choices=[('JH', 'Medicine'), ('MJ', 'Life')])),
                ('title', models.CharField(max_length=256)),
                ('picture', models.ImageField(blank=True, upload_to='item_images')),
                ('text', models.TextField()),
                ('user', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(verbose_name='생성일', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='수정일', auto_now=True)),
                ('category', models.ForeignKey(null=True, to='line.Category', blank=True)),
            ],
            options={
                'verbose_name': '글',
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(to='line.Item'),
            preserve_default=True,
        ),
    ]
