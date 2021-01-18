# Generated by Django 2.2.17 on 2021-01-13 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('js_components', '0028_auto_20201014_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Float',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_components_float', serialize=False, to='cms.CMSPlugin')),
                ('alignment', models.CharField(blank=True, default='', max_length=255, verbose_name='Alignment')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
