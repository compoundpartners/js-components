# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models, forms
from .constants import (
    HIDE_PROMO,
    HIDE_TWITTER,
)

class PromoUnitPlugin(CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/promo_%s.html'
    name = _('Promo Unit')
    model = models.PromoUnit
    form = forms.PromoUnitForm
    render_template = 'js_components/promo.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        if instance.layout:
            return self.TEMPLATE_NAME % instance.layout
        return self.render_template

if not HIDE_PROMO:
    plugin_pool.register_plugin(PromoUnitPlugin)


class TwitterFeedPlugin(CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/twitter_%s.html'
    name = _('Twitter Feed')
    model = models.TwitterFeed
    form = forms.TwitterFeedForm
    render_template = 'js_components/twitter.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        if instance.layout:
            return self.TEMPLATE_NAME % instance.layout
        return self.render_template

if not HIDE_TWITTER:
    plugin_pool.register_plugin(TwitterFeedPlugin)


