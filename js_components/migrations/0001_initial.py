# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-22 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_icon.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_components_calltoaction', serialize=False, to='cms.CMSPlugin')),
                ('icon', djangocms_icon.fields.Icon(blank=True, default='fa-', max_length=255, verbose_name='Icon')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='Content')),
                ('link_url', models.CharField(blank=True, max_length=255, verbose_name='Link URL')),
                ('link_text', models.CharField(blank=True, max_length=255, verbose_name='Link Text')),
                ('open_in_new_window', models.BooleanField(default=False, verbose_name='Open in new window')),
                ('layout', models.CharField(blank=True, default='', max_length=60, verbose_name='layout')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
