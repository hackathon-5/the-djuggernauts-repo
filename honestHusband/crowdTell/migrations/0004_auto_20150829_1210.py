# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdTell', '0003_auto_20150829_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to=b'uploads/%Y/%m/%d/')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='picture',
            name='person',
        ),
        migrations.RemoveField(
            model_name='question',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='answer',
            name='picture_question',
            field=models.ForeignKey(default=1, to='crowdTell.PictureQuestion'),
            preserve_default=False,
        ),
    ]
