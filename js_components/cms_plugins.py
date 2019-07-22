# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models, forms
from .constants import (
    HIDE_PROMO,
    HIDE_TWITTER,
    HIDE_COUNTERS,
    HIDE_RAWHTML,
)

class LayoutMixin():

    def get_layout(self, context, instance, placeholder):
        return instance.layout

    def get_render_template(self, context, instance, placeholder):
        layout = self.get_layout(context, instance, placeholder)
        if layout:
            template = self.TEMPLATE_NAME % layout
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class PromoUnitPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/promo_%s.html'
    name = _('Promo Unit')
    model = models.PromoUnit
    form = forms.PromoUnitForm
    render_template = 'js_components/promo.html'

    fieldsets = [
        (None, {
            'fields': (
                'layout',
                'title',
                'subtitle',
                'image',
                'icon',
                'content',
                'link_text',
                'link_url',
                ('file_src', 'show_filesize'),
                'open_in_new_window',
            )
        }),
    ]


if not HIDE_PROMO:
    plugin_pool.register_plugin(PromoUnitPlugin)


class TwitterFeedPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/twitter_%s.html'
    name = _('Twitter Feed')
    model = models.TwitterFeed
    form = forms.TwitterFeedForm
    render_template = 'js_components/twitter.html'

if not HIDE_TWITTER:
    plugin_pool.register_plugin(TwitterFeedPlugin)


class CountersContainerPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/counters_%s.html'
    name = _('Counters Container (DO NOT USE, NEED REMOVE)')
    model = models.CountersContainer
    form = forms.CountersContainerForm
    render_template = 'js_components/counters.html'
    allow_children = True
    child_classes = ['CounterPlugin']
    parent_classes = ['Bootstrap4GridRowPlugin']


class CounterPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/counter_%s.html'
    name = _('Counter')
    model = models.Counter
    form = forms.CounterForm
    render_template = 'js_components/counter.html'


if not HIDE_COUNTERS:
    plugin_pool.register_plugin(CountersContainerPlugin)
    plugin_pool.register_plugin(CounterPlugin)
    #if 'Bootstrap4GridRowPlugin' in plugin_pool.plugins:
        #plugin_pool.plugins['Bootstrap4GridRowPlugin'].child_classes.append('CountersContainerPlugin')


class RawHTMLPlugin(CMSPluginBase):
    module = 'JumpSuite Componens'
    name = _('Raw HTML')
    model = models.RawHTML
    render_template = 'js_components/html.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


if not HIDE_RAWHTML:
    plugin_pool.register_plugin(RawHTMLPlugin)
