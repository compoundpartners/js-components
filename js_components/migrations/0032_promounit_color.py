# Generated by Django 2.2.20 on 2021-04-29 15:44

from django.db import migrations
import js_color_picker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('js_components', '0031_auto_20210319_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='promounit',
            name='color',
            field=js_color_picker.fields.RGBColorField(blank=True, colors={}, mode='both', null=True, verbose_name='Color'),
        ),
    ]
