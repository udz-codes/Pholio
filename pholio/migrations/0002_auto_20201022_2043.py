# Generated by Django 3.0.7 on 2020-10-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pholio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
    ]