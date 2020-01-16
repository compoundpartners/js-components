# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from . import models
from .constants import (
    PROMO_LAYOUTS,
    TWITTER_LAYOUTS,
    COUNTERS_LAYOUTS,
)

PROMO_LAYOUT_CHOICES = PROMO_LAYOUTS
if len(PROMO_LAYOUT_CHOICES) == 0 or len(PROMO_LAYOUT_CHOICES[0]) != 2:
    PROMO_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + PROMO_LAYOUTS)), ('default',) + PROMO_LAYOUTS)

TWITTER_LAYOUT_CHOICES = TWITTER_LAYOUTS
if len(TWITTER_LAYOUT_CHOICES) == 0 or len(TWITTER_LAYOUT_CHOICES[0]) != 2:
    TWITTER_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + TWITTER_LAYOUTS)), ('default',) + TWITTER_LAYOUTS)

COUNTERS_LAYOUT_CHOICES = COUNTERS_LAYOUTS
if len(COUNTERS_LAYOUT_CHOICES) == 0 or len(COUNTERS_LAYOUT_CHOICES[0]) != 2:
    COUNTERS_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + COUNTERS_LAYOUTS)), ('default',) + COUNTERS_LAYOUTS)


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
