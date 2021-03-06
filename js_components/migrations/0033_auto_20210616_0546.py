# Generated by Django 2.2.24 on 2021-06-16 05:46

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('js_components', '0032_promounit_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='promounit',
            name='svg',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.File', verbose_name='SVG Image'),
        ),
    ]
