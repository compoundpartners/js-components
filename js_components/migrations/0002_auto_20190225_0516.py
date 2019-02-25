# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-25 05:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_icon.fields
import djangocms_text_ckeditor.fields
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('js_components', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoUnit',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_components_promounit', serialize=False, to='cms.CMSPlugin')),
                ('icon', djangocms_icon.fields.Icon(blank=True, default='fa-', max_length=255, verbose_name='Icon')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='Content')),
                ('link_url', models.CharField(blank=True, max_length=255, verbose_name='Link URL')),
                ('link_text', models.CharField(blank=True, max_length=255, verbose_name='Link Text')),
                ('open_in_new_window', models.BooleanField(default=False, verbose_name='Open in new window')),
                ('layout', models.CharField(blank=True, default='', max_length=60, verbose_name='layout')),
                ('file_src', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.File', verbose_name='File')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='calltoaction',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='CallToAction',
        ),
    ]
