# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_styledlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styledlink',
            name='mailto',
            field=models.EmailField(max_length=254, help_text='An email address. This will override an external url.', blank=True, verbose_name='email address', null=True),
        ),
        migrations.AlterField(
            model_name='styledlink',
            name='page_destination',
            field=models.CharField(max_length=64, help_text='Use this to specify an intra-page link. Can be used for the <em>current page</em> or with a specific internal destination. Do <strong>not</strong> include a leading “#”. To trigger modals prepend "modal-" to the movie id.', blank=True, verbose_name='intra-page destination'),
        ),
        migrations.AlterField(
            model_name='styledlink',
            name='styles',
            field=models.ManyToManyField(default=None, help_text='Optional. Choose one or more styles for this link.', verbose_name='link style', related_name='styled_link_style', blank=True, to='djangocms_styledlink.StyledLinkStyle'),
        ),
    ]
