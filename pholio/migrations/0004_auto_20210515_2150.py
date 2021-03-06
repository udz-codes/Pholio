# Generated by Django 3.2 on 2021-05-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pholio', '0003_auto_20201031_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
