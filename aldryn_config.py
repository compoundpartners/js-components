from aldryn_client import forms

class Form(forms.BaseForm):
    hide_promo = forms.CheckboxField(
        'Hide Promo Unit', required=False, initial=False
    )
    hide_promo_rollover = forms.CheckboxField(
        'Hide rollover field fro Promo Unit', required=False, initial=True
    )
    hide_twitter = forms.CheckboxField(
        'Hide Twitter plugin', required=False, initial=False
    )
    twitter_app_key = forms.CharField(
        'Twitter App Key', required=False
    )
    twitter_app_secret = forms.CharField(
        'Twitter App Secret', required=False
    )
    twitter_oauth_token = forms.CharField(
        'Twitter OAuth Tocken', required=False
    )
    twitter_oauth_secret = forms.CharField(
        'Twitter OAuth Secret', required=False
    )
    hide_counters = forms.CheckboxField(
        'Hide Counters plugin', required=False, initial=False
    )
    hide_rawhtml = forms.CheckboxField(
        'Hide Raw HTML plugin', required=False, initial=False
    )
    hide_gated_content = forms.CheckboxField(
        'Hide Gated Content plugin', required=False, initial=True
    )

    def to_settings(self, data, settings):
        settings['COMPONENTS_HIDE_PROMO'] = int(data['hide_promo'])
        settings['COMPONENTS_HIDE_PROMO_ROLLOVER'] = int(data['hide_promo_rollover'])
        settings['COMPONENTS_HIDE_TWITTER'] = int(data['hide_twitter'])
        if data['twitter_app_key']:
            settings['TWITTER_APP_KEY'] = data['twitter_app_key']
        if data['twitter_app_secret']:
            settings['TWITTER_APP_SECRET'] = data['twitter_app_secret']
        if data['twitter_oauth_token']:
            settings['TWITTER_OAUTH_TOKEN'] = data['twitter_oauth_token']
        if data['twitter_oauth_secret']:
            settings['TWITTER_OAUTH_SECRET'] = data['twitter_oauth_secret']
        settings['COMPONENTS_HIDE_COUNTERS'] = int(data['hide_counters'])
        settings['COMPONENTS_HIDE_RAWHTML'] = int(data['hide_rawhtml'])
        settings['COMPONENTS_HIDE_GATED_CONTENT'] = int(data['hide_gated_content'])
        return settings
