# Generated by Django 4.2.6 on 2023-10-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='design',
            options={'verbose_name': 'Design', 'verbose_name_plural': 'Designs'},
        ),
        migrations.RemoveField(
            model_name='design',
            name='short_description',
        ),
    ]
