# Generated by Django 4.2 on 2023-04-16 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantations', '0016_alter_ground_created_by_alter_ground_updated_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalirrigation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='historicalplantation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='historicalplantation',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='irrigation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Nombre'),
        ),
    ]