# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(related_name='comments', to='line.Item'),
            preserve_default=True,
        ),
    ]
