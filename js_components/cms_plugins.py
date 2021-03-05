# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import functools
import six
from django.utils.translation import ugettext_lazy as _
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from cms.plugin_base import CMSPluginBase, CMSPluginBaseMetaclass
from cms.plugin_pool import plugin_pool
from . import models, forms
from .utils.urlmatch import urlmatch
from .constants import (
    HIDE_PROMO,
    HIDE_PROMO_ROLLOVER,
    HIDE_PROMO_VIDEO,
    HIDE_TWITTER,
    HIDE_COUNTERS,
    HIDE_RAWHTML,
    HIDE_GATED_CONTENT,
    HIDE_FLOAT,
    CUSTOM_PLUGINS,
    PROMO_CHILD_CLASSES,
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
    allow_children = True if PROMO_CHILD_CLASSES else False
    child_classes = PROMO_CHILD_CLASSES

    main_fields = [
        'layout',
        'title',
        'subtitle',
        'image',
        'icon',
        'content',
        'rollover_content',
        'background_video',
        'link_text',
        'link_url',
        ('file_src', 'show_filesize'),
        'open_in_new_window',
    ]
    if HIDE_PROMO_ROLLOVER:
        main_fields.remove('rollover_content')
    if HIDE_PROMO_VIDEO:
        main_fields.remove('background_video')

    fieldsets = [
        (None, {
            'fields': main_fields
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'modal_id',
                'attributes',
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
            'html': instance.body,
        })
        return context


class RawHTMLWithIDPlugin(CMSPluginBase):
    module = 'JumpSuite Componens'
    name = _('Raw HTML with ID')
    model = models.RawHTMLWithID
    render_template = 'js_components/html.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        html = instance.body
        for param in instance.parameters.split(','):

            param = param.strip()
            key = '[%s]' % param.upper()
            html = html.replace(key, request.GET.get(param) or request.POST.get(param, ''))
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'html': html,
        })
        return context


if not HIDE_RAWHTML:
    plugin_pool.register_plugin(RawHTMLPlugin)
    plugin_pool.register_plugin(RawHTMLWithIDPlugin)



@plugin_pool.register_plugin
class CustomPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/custom_%s.html'
    name = _('Custom')
    model = models.Custom
    form = forms.CustomForm
    render_template = 'js_components/custom.html'

    def get_form(self, request, obj=None, **kwargs):
        Form = super().get_form(request, obj=None, **kwargs)
        if self.name in CUSTOM_PLUGINS:
            Form.plugin_name=self.name
        return Form

for name, parameters in CUSTOM_PLUGINS.items():
    p = type(
        str(name.replace(' ', '') + 'Plugin'),
        (CustomPlugin,),
        {'name': name},
    )
    plugin_pool.register_plugin(p)


class GatedContentPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/gated_content_%s.html'
    name = _('Gated Content')
    model = models.GatedContent
    form = forms.GatedContentForm
    render_template = 'js_components/gated_content.html'
    allow_children = True

if not HIDE_GATED_CONTENT:
    plugin_pool.register_plugin(GatedContentPlugin)


@plugin_pool.register_plugin
class AnimatePlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/animate_%s.html'
    name = _('Animate')
    model = models.Animate
    form = forms.AnimateForm
    render_template = 'js_components/animate.html'
    allow_children = True


@plugin_pool.register_plugin
class JSFolderPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Componens'
    TEMPLATE_NAME = 'js_components/folder_%s.html'
    name = _('Filer listing')
    model = models.Folder
    form = forms.FolderForm
    render_template = 'js_components/folder.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        files = []
        if instance.folder:
            files = instance.folder.files.all()
            if instance.order_by:
                files = files.order_by(instance.order_by)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'files': files,
        })
        return context


@plugin_pool.register_plugin
class IncludeExcludeContainer(CMSPluginBase):
    module = 'JumpSuite Componens'
    name = _('Include/Exclude Container')
    model = models.IncludeExcludeContainer
    render_template = 'js_components/container.html'
    change_form_template = 'admin/js_components/change_form_container.html'
    allow_children = True
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']
        url = '%s://%s%s' % (request.scheme, request.META['HTTP_HOST'], request.path)
        is_shown = urlmatch(','.join(instance.include.split('\n')), url) and not urlmatch(','.join(instance.exclude.split('\n')), url)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'is_shown': is_shown,
        })
        return context


class FloatPlugin(CMSPluginBase):
    module = 'JumpSuite Componens'
    name = _('Float Container')
    model = models.Float
    form = forms.FloatForm
    render_template = 'js_components/float.html'
    change_form_template = 'admin/js_components/float.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'alignment': instance.alignment,
        })
        return context

if not HIDE_FLOAT:
    plugin_pool.register_plugin(FloatPlugin)
