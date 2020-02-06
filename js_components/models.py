# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_icon.fields import Icon
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from twython import Twython, TwythonError
from dateutil.parser import parse
from filer.models.filemodels import File
from djangocms_attributes_field import fields


from .constants import (
    TWITTER_APP_KEY,
    TWITTER_APP_SECRET,
    TWITTER_OAUTH_TOKEN,
    TWITTER_OAUTH_SECRET,
    TWITTER_CACHE_TIMEOUT,
    TWYTHON_KWARGS,
)

class AttributesField(fields.AttributesField):
    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = _('Attributes')
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        super(AttributesField, self).__init__(*args, **kwargs)


class Video(File):
    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        filename_extensions = ['.dv', '.mov', '.mp4', '.avi', '.wmv',]
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions


class FilerVideoField(FilerFileField):
    default_model_class = Video


@python_2_unicode_compatible
class PromoUnit(CMSPlugin):
    icon = Icon(
        verbose_name=_('Icon'),
        blank=True,
        default=''
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
        verbose_name=_('Title'),
        null=True,
        blank=True,
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name=_('Subtitle'),
        null=True,
        blank=True,
    )
    content = HTMLField(
        verbose_name=_('Content'),
        default='',
        blank=True
    )
    rollover_content = HTMLField(
        verbose_name=_('Rollover Content'),
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
    show_filesize = models.BooleanField(
        default=True,
        verbose_name=_('Show Filesize')
    )
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )
    attributes = AttributesField()

    def __str__(self):
        return self.title or str(self.pk)


@python_2_unicode_compatible
class TwitterFeed(CMSPlugin):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
        blank=True,
        null=True,
    )
    username = models.CharField(
        max_length=255,
        verbose_name=_('twitter username')
    )
    count = models.IntegerField(
        default=3,
        verbose_name=_('number of tweets to show')
    )
    followers = models.IntegerField(
        editable=False,
        null=True
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )

    def __str__(self):
        return self.username

    def tweets(self):
        cache_key = 'use-twitter-cache'
        if not cache.get(cache_key, False):
            cache.set(cache_key, True, TWITTER_CACHE_TIMEOUT)
            self.save()
        return self.tweetcache_set.all().order_by('-date')[:self.count]

    def get_latest_twitter_data(self):

        twitter = Twython(
            app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_SECRET,
            oauth_token=TWITTER_OAUTH_TOKEN,
            oauth_token_secret=TWITTER_OAUTH_SECRET
        )

        try:
            # count is number of tweets, including RTs and replies, so we get
            # ten times as many so that we can then reduce down to the
            # requested count.
            timeline = twitter.get_user_timeline(
                screen_name=self.username,
                count=self.count * 10,
                include_entities=True,
                include_rts=False,
                exclude_replies=True,
                tweet_mode='extended'
            )
            print(timeline[0])
        except TwythonError:
            return {'tweets': [], 'followers': 0}

        tweets = []
        for t in timeline:
            d = parse(t["created_at"], ignoretz=True)
            words = t['full_text'].split(' ')
            t['full_text'] = ' '.join(words[0:-1])
            link = words[-1]
            media = []
            if 'media' in t['entities']:
                for url in t['entities']['media']:
                    if url['url'] != link:
                        media.append(url)
                t['entities']['media'] = media
            text = Twython.html_for_tweet(t, **TWYTHON_KWARGS)

            # Process images into links
            # Twython's html_for_tweet function doesn't handle these.
            #try:
            #    for url in t['entities']['media']:
            #        html_link = '<a href="' + \
            #            '%s" rel="nofollow" target="_blank">%s</a>' % (
            #                url['expanded_url'], url['display_url'])
            #        text = text.replace(url['url'], html_link)
            #except KeyError:
            #    pass

            # strip out manual RTs
            if text[0:2] != 'RT':
                tweets.append({'date': d, 'text': text, 'tweet_link': link})

        if tweets:
            return {
                'tweets': tweets,
                'followers': t['user']['followers_count']
            }
        else:
            return {'tweets': [], 'followers': 0}

    # we update the cache separately (also makes saving follower count into
    # self model easier.

    def update_cache(self, tweets):
        TweetCache.objects.filter(plugin_instance=self).delete()

        for t in tweets:
            tc = TweetCache(
                plugin_instance=self, text=t['text'], date=t['date'], tweet_link=t['tweet_link'])
            tc.save()

    def save(self):
        data = self.get_latest_twitter_data()
        self.followers = data['followers']
        super(TwitterFeed, self).save()
        if len(data['tweets']) and any([t['text'] for t in data['tweets']]):
            self.update_cache(data['tweets'])


class TweetCache(models.Model):
    plugin_instance = models.ForeignKey(TwitterFeed, models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()
    tweet_link = models.CharField(max_length=60, blank=True)


#need to remove
@python_2_unicode_compatible
class CountersContainer(CMSPlugin):
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )
    def __str__(self):
        return str(self.pk)


@python_2_unicode_compatible
class Counter(CMSPlugin):
    body = models.CharField(
        _('Title'),
        max_length=255,
        null=True,
        blank=True
    )
    counter = models.CharField(
        _('counter'),
        max_length=255
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    icon = Icon(
        verbose_name=_('Icon'),
        null=True,
        blank=True
    )
    prefix = models.CharField(
        _('prefix'),
        max_length=255,
        null=True,
        blank=True
    )
    suffix = models.CharField(
        _('suffix'),
        max_length=255,
        null=True,
        blank=True
    )
    content = HTMLField(
        verbose_name=_('Content'),
        default='',
        blank=True
    )
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )


    def __str__(self):
        return str(self.pk)


@python_2_unicode_compatible
class RawHTML(CMSPlugin):
    body = models.TextField(
        _('HTML body')
    )

    def __str__(self):
        return str(self.pk)


@python_2_unicode_compatible
class RawHTMLWithID(CMSPlugin):
    body = models.TextField(
        _('HTML body')
    )
    parameters = models.CharField(
        _('parameters'),
        max_length=255,
        null=True,
        blank=True,
        help_text=_('comma separated'),
    )

    def __str__(self):
        return self.parameters


@python_2_unicode_compatible
class Custom(CMSPlugin):
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )


    def __str__(self):
        return str(self.pk)
