# Generated by Django 2.2.10 on 2020-06-10 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('js_components', '0023_gatedcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animate',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_components_animate', serialize=False, to='cms.CMSPlugin')),
                ('layout', models.CharField(blank=True, default='', max_length=60, verbose_name='layout')),
                ('animation', models.CharField(max_length=60, verbose_name='animation')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=0, help_text='slow 2s/slower 3s/fast 800ms/faster  500ms', verbose_name='duration [ms]')),
                ('delay', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='delay [ms]')),
                ('repeat', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='repeat')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]