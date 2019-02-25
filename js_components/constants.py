# -*- coding: utf-8 -*-

from django.conf import settings

HIDE_PROMO = getattr(
    settings,
    'COMPONENTS_HIDE_PROMO',
    False,
)
PROMO_LAYOUTS = getattr(
    settings,
    'COMPONENTS_PROMO_LAYOUTS',
    (),
)
