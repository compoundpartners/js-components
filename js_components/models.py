# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_icon.fields import Icon
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


@python_2_unicode_compatible
class PromoUnit(CMSPlugin):
    icon = Icon(
        verbose_name=_('Icon'),
        blank=True,
        default='fa-'
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    file_src = FilerFileField(
        verbose_name=_('File'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title')
    )
    content = HTMLField(
        verbose_name=_('Content'),
        default='',
        blank=True
    )
    link_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Link URL')
    )
    link_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Link Text')
    )
    open_in_new_window = models.BooleanField(
        default=False,
        verbose_name=_('Open in new window')
    )
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )

    def __str__(self):
        return self.title
