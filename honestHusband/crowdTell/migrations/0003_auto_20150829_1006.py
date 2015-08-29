# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdTell', '0002_person_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='friend',
        ),
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='crowdTell.Person'),
        ),
    ]
