from aldryn_client import forms

class Form(forms.BaseForm):
    hide_promo = forms.CheckboxField(
        'Hide Promo Unit', required=False, initial=False
    )

    def to_settings(self, data, settings):
        settings['COMPONENTS_HIDE_PROMO'] = int(data['hide_promo'])
        return settings
