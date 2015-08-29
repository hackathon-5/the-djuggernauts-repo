# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdTell', '0004_auto_20150829_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturequestion',
            name='person',
            field=models.ForeignKey(default=1, to='crowdTell.Person'),
            preserve_default=False,
        ),
    ]
