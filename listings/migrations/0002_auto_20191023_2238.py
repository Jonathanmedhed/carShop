# Generated by Django 2.2.6 on 2019-10-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='body',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
