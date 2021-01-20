# -*- coding: utf-8 -*-

from django.conf import settings

HIDE_PROMO = getattr(
    settings,
    'COMPONENTS_HIDE_PROMO',
    False,
)
HIDE_PROMO_ROLLOVER = getattr(
    settings,
    'COMPONENTS_HIDE_PROMO_ROLLOVER',
    True,
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
HIDE_COUNTERS = getattr(
    settings,
    'COMPONENTS_HIDE_COUNTERS',
    False,
)
COUNTERS_LAYOUTS = getattr(
    settings,
    'COMPONENTS_COUNTERS_LAYOUTS',
    (),
)
CUSTOM_LAYOUTS = getattr(
    settings,
    'COMPONENTS_CUSTOM_LAYOUTS',
    (),
)
CUSTOM_PLUGINS = getattr(
    settings,
    'COMPONENTS_CUSTOM_PLUGINS',
    {},
)
HIDE_RAWHTML = getattr(
    settings,
    'COMPONENTS_HIDE_RAWHTML',
    False,
)
HIDE_FLOAT = getattr(
    settings,
    'COMPONENTS_HIDE_FLOAT',
    True,
)
HIDE_GATED_CONTENT = getattr(
    settings,
    'COMPONENTS_HIDE_GATED_CONTENT',
    True,
)
GATED_CONTENT_LAYOUTS = getattr(
    settings,
    'COMPONENTS_GATED_CONTENT_LAYOUTS',
    (),
)
TWYTHON_KWARGS = getattr(
    settings,
    'COMPONENTS_TWYTHON_KWARGS',
    {'use_display_url': True},
)
TWITTER_CACHE_TIMEOUT = getattr(
    settings,
    'COMPONENTS_TWITTER_CACHE_TIMEOUT',
    60*60*24,
)
PROMO_CHILD_CLASSES = getattr(
    settings,
    'COMPONENTS_PROMO_CHILD_CLASSES',
    []
)

ALL_ANIMATIONS = [
    # Attention seekers
  'bounce',
  'flash',
  'pulse',
  'rubberBand',
  'shakeX',
  'shakeY',
  'headShake',
  'swing',
  'tada',
  'wobble',
  'jello',
  'heartBeat',
    # Back entrances
  'backInDown',
  'backInLeft',
  'backInRight',
  'backInUp',
    # Back exits
  'backOutDown',
  'backOutLeft',
  'backOutRight',
  'backOutUp',
    # Bouncing entrances
  'bounceIn',
  'bounceInDown',
  'bounceInLeft',
  'bounceInRight',
  'bounceInUp',
    # Bouncing exits
  'bounceOut',
  'bounceOutDown',
  'bounceOutLeft',
  'bounceOutRight',
  'bounceOutUp',
    # Fading entrances
  'fadeIn',
  'fadeInDown',
  'fadeInDownBig',
  'fadeInLeft',
  'fadeInLeftBig',
  'fadeInRight',
  'fadeInRightBig',
  'fadeInUp',
  'fadeInUpBig',
  'fadeInTopLeft',
  'fadeInTopRight',
  'fadeInBottomLeft',
  'fadeInBottomRight',
    # Fading exits
  'fadeOut',
  'fadeOutDown',
  'fadeOutDownBig',
  'fadeOutLeft',
  'fadeOutLeftBig',
  'fadeOutRight',
  'fadeOutRightBig',
  'fadeOutUp',
  'fadeOutUpBig',
  'fadeOutTopLeft',
  'fadeOutTopRight',
  'fadeOutBottomRight',
  'fadeOutBottomLeft',
    # Flippers
  'flip',
  'flipInX',
  'flipInY',
  'flipOutX',
  'flipOutY',
    # Lightspeed
  'lightSpeedInRight',
  'lightSpeedInLeft',
  'lightSpeedOutRight',
  'lightSpeedOutLeft',
    # Rotating entrances
  'rotateIn',
  'rotateInDownLeft',
  'rotateInDownRight',
  'rotateInUpLeft',
  'rotateInUpRight',
    # Rotating exits
  'rotateOut',
  'rotateOutDownLeft',
  'rotateOutDownRight',
  'rotateOutUpLeft',
  'rotateOutUpRight',
    # Specials
  'hinge',
  'jackInTheBox',
  'rollIn',
  'rollOut',
    # Zooming entrances
  'zoomIn',
  'zoomInDown',
  'zoomInLeft',
  'zoomInRight',
  'zoomInUp',
    # Zooming exits
  'zoomOut',
  'zoomOutDown',
  'zoomOutLeft',
  'zoomOutRight',
  'zoomOutUp',
    # Sliding entrances
  'slideInDown',
  'slideInLeft',
  'slideInRight',
  'slideInUp',
    # Sliding exits
  'slideOutDown',
  'slideOutLeft',
  'slideOutRight',
  'slideOutUp']

ENABLED_ANIMATIONS = getattr(
    settings,
    'COMPONENTS_ENABLED_ANIMATIONS',
    ('*'),
)
DISABLED_ANIMATIONS = getattr(
    settings,
    'COMPONENTS_DISABLED_ANIMATIONS',
    (),
)
import re
enabled = re.findall("(%s)" % "|".join(map(lambda x: x.strip().replace('*', '\S*'), ENABLED_ANIMATIONS)), ' '.join(ALL_ANIMATIONS), re.I)
disabled = re.findall("(%s)" % "|".join(map(lambda x: x.strip().replace('*', '\S*'), DISABLED_ANIMATIONS)), ' '.join(enabled), re.I)
ANIMATIONS = list(set(enabled) - set(disabled))
ANIMATIONS.sort()
