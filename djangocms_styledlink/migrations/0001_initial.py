# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyledLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='cms.CMSPlugin', serialize=False)),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='link text', default='', help_text='Required. The text that is linked.')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title', default='', help_text='Optional. If provided, will provide a tooltip for the link.')),
                ('int_destination_id', models.PositiveIntegerField(null=True, blank=True)),
                ('page_destination', models.CharField(max_length=64, blank=True, verbose_name='intra-page destination', help_text='Use this to specify an intra-page link. Can be used for the <em>current page</em> or with a specific internal destination. Do <strong>not</strong> include a leading “#”.')),
                ('int_hash', models.BooleanField(default=False)),
                ('ext_destination', models.TextField(blank=True, verbose_name='external destination', default='')),
                ('ext_follow', models.BooleanField(verbose_name='follow external link?', default=True, help_text='Let search engines follow this hyperlink?')),
                ('mailto', models.EmailField(null=True, max_length=75, blank=True, verbose_name='email address', help_text='An email address. This will override an external url.')),
                ('target', models.CharField(default='', verbose_name='target', help_text='Optional. Specify if this link should open in a new tab or window.', max_length=100, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], blank=True)),
                ('int_destination_type', models.ForeignKey(null=True, to='contenttypes.ContentType', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='StyledLinkStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('label', models.CharField(max_length=32, verbose_name='label', default='', help_text='The internal name of this link style.')),
                ('link_class', models.CharField(max_length=32, verbose_name='link class', default='', help_text='The class to add to this link (do NOT preceed with a ".").')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='styledlink',
            name='styles',
            field=models.ManyToManyField(null=True, related_name='styled_link_style', default=None, verbose_name='link style', help_text='Optional. Choose one or more styles for this link.', to='djangocms_styledlink.StyledLinkStyle', blank=True),
            preserve_default=True,
        ),
    ]
