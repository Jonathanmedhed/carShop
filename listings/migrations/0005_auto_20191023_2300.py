# Generated by Django 2.2.6 on 2019-10-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20191023_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='cc',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
