# Generated by Django 3.0.7 on 2020-10-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pholio', '0002_auto_20201022_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='certificate',
            field=models.URLField(blank=True, null=True),
        ),
    ]
