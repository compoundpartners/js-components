# Generated by Django 2.2.14 on 2020-09-04 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('js_components', '0025_folder'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncludeExcludeContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_components_includeexcludecontainer', serialize=False, to='cms.CMSPlugin')),
                ('include', models.TextField(blank=True, default='*', help_text='URL without domain should starts withou first slash (/) (e.g. test/me). Use asterisk (*) to show/hode on multiple pages (e.g. blog/* or *://test.com/*)', verbose_name='Show on only these pages')),
                ('exclude', models.TextField(blank=True, default='', verbose_name='Hide onthese pages')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]