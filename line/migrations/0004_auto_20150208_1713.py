# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0003_auto_20150208_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
