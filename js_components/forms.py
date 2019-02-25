# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from . import models
from .constants import PROMO_LAYOUTS

LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_').join(['', '.html']), PROMO_LAYOUTS)), PROMO_LAYOUTS)


class PromoUnitForm(forms.ModelForm):

    layout = forms.ChoiceField(LAYOUT_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(PromoUnitForm, self).__init__(*args, **kwargs)
        if len(PROMO_LAYOUTS) == 0:
            self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.PromoUnit
        fields = ['icon', 'image', 'file_src', 'title', 'content',
            'link_url', 'link_text', 'open_in_new_window', 'layout']
