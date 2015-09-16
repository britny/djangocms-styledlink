# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_styledlink', '0002_auto_20150911_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='styledlink',
            name='open_in_modal',
            field=models.BooleanField(verbose_name='Open video in modal', default=False, help_text='Whether the video will open in a modal overlay or behaves just like a link.'),
        ),
        migrations.AddField(
            model_name='styledlink',
            name='video_link',
            field=models.CharField(null=True, default='', help_text='Link to an external video (Youtube or Vimeo). Other link types have priority, empty them to get the video link to work', max_length=2048, verbose_name='Video url', blank=True),
        ),
    ]
