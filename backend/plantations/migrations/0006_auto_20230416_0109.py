# Generated by Django 3.2 on 2023-04-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantations', '0005_auto_20230416_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalplantation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]