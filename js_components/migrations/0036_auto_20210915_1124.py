# Generated by Django 2.2.24 on 2021-09-15 11:24

from django.db import migrations, models
import js_color_picker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('js_components', '0035_auto_20210816_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='title'),
        ),
    ]