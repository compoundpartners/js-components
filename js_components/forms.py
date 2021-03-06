# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from . import models
from .constants import (
    PROMO_LAYOUTS,
    TWITTER_LAYOUTS,
    COUNTERS_LAYOUTS,
    CUSTOM_LAYOUTS,
    GATED_CONTENT_LAYOUTS,
    LIGHTBOX_LAYOUTS,
    ANIMATIONS,
    CUSTOM_PLUGINS,
)

try:
    from js_custom_fields.forms import CustomFieldsFormMixin
except:
    class CustomFieldsFormMixin(object):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'custom_fields' in self.fields:
                self.fields['custom_fields'].widget = forms.HiddenInput()

def get_choices(choices, add_default=True):
    if len(choices) == 0 or len(choices[0]) != 2:
        if add_default:
            return zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + choices)), ('default',) + choices)
        return zip(list(map(lambda s: slugify(s).replace('-', '_'), choices)), choices)
    return choices

PROMO_LAYOUT_CHOICES = get_choices(PROMO_LAYOUTS)

TWITTER_LAYOUT_CHOICES = get_choices(TWITTER_LAYOUTS)

COUNTERS_LAYOUT_CHOICES = get_choices(COUNTERS_LAYOUTS)

CUSTOM_LAYOUT_CHOICES = get_choices(CUSTOM_LAYOUTS)

GATED_CONTENT_LAYOUT_CHOICES = get_choices(GATED_CONTENT_LAYOUTS)

LIGHTBOX_LAYOUT_CHOICES = get_choices(LIGHTBOX_LAYOUTS)

ANIMATION_CHOICES = zip(ANIMATIONS, ANIMATIONS)


ORDER_BY_CHOICES = (
  ('', '--------'),
  ('uploaded_at', 'Date'),
  ('name', 'Name'),
  ('original_filename', 'File Name'),
)

FLOAT_CHOICES = (
  ('', '--------'),
  ('left', 'Left'),
  ('center', 'Center'),
  ('right', 'Right'),
)


class PromoUnitForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=PROMO_LAYOUT_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(PromoUnitForm, self).__init__(*args, **kwargs)
        if len(PROMO_LAYOUTS) == 0:
            self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.PromoUnit
        fields = ['icon', 'image', 'file_src', 'title', 'subtitle', 'content',
            'link_url', 'link_text', 'open_in_new_window', 'layout']


class TwitterFeedForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=TWITTER_LAYOUT_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(TwitterFeedForm, self).__init__(*args, **kwargs)
        if len(TWITTER_LAYOUTS) == 0:
            self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.TwitterFeed
        fields = ['title', 'username', 'count', 'image', 'layout']


class CountersContainerForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=COUNTERS_LAYOUT_CHOICES, required=False)

    #def __init__(self, *args, **kwargs):
        #super(CountersContainerForm, self).__init__(*args, **kwargs)
        #if len(COUNTERS_LAYOUTS) == 0:
            #self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.CountersContainer
        fields = ['layout']

class CounterForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=COUNTERS_LAYOUT_CHOICES, required=False)

    #def __init__(self, *args, **kwargs):
        #super(CountersContainerForm, self).__init__(*args, **kwargs)
        #if len(COUNTERS_LAYOUTS) == 0:
            #self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.Counter
        fields = '__all__'


class CustomForm(CustomFieldsFormMixin, forms.ModelForm):

    layout = forms.ChoiceField(required=False)

    custom_fields = 'get_custom_fields'
    plugin_name = None

    class Meta:
        model = models.Custom
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['layout'].choices = self.get_layouts()

    def get_custom_fields(self):
        return {}

    def get_layouts(self):
        if self.plugin_name:
            return get_choices(CUSTOM_PLUGINS.get(self.plugin_name, {}).get('layouts', (self.plugin_name,)), add_default=False)
        return CUSTOM_LAYOUT_CHOICES

    def get_custom_fields(self):
        if self.plugin_name:
            return CUSTOM_PLUGINS.get(self.plugin_name, {}).get('fields', {})
        return {}


class GatedContentForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=GATED_CONTENT_LAYOUT_CHOICES, required=False)

    class Meta:
        model = models.Custom
        fields = ['layout']


class LightboxForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=LIGHTBOX_LAYOUT_CHOICES, required=False)

    class Meta:
        model = models.Lightbox
        fields = '__all__'


class AnimateForm(forms.ModelForm):

    animation = forms.ChoiceField(choices=ANIMATION_CHOICES)

    class Meta:
        model = models.Animate
        exclude = ['layout']


class FolderForm(forms.ModelForm):

    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, required=False)

    class Meta:
        model = models.Folder
        exclude = ['layout']


class FloatForm(forms.ModelForm):

    alignment = forms.ChoiceField(choices=FLOAT_CHOICES, required=False)

    class Meta:
        model = models.Float
        fields = '__all__'
