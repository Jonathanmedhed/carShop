# Generated by Django 2.2.6 on 2019-11-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_listing_is_in_spotlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_extra',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_extra2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]