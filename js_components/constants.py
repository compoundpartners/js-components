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
HIDE_TWITTER = getattr(
    settings,
    'COMPONENTS_HIDE_TWITTER',
    False,
)
TWITTER_LAYOUTS = getattr(
    settings,
    'COMPONENTS_TWITTER_LAYOUTS',
    (),
)
TWITTER_APP_KEY = getattr(
    settings,
    'TWITTER_APP_KEY',
    False,
)
TWITTER_APP_SECRET = getattr(
    settings,
    'TWITTER_APP_SECRET',
    False,
)
TWITTER_OAUTH_TOKEN = getattr(
    settings,
    'TWITTER_OAUTH_TOKEN',
    False,
)
TWITTER_OAUTH_SECRET = getattr(
    settings,
    'TWITTER_OAUTH_SECRET',
    False,
)
