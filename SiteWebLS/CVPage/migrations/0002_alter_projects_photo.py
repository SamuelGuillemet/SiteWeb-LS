# Generated by Django 4.0.3 on 2022-05-07 00:49

import CVPage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='photo',
            field=models.ImageField(upload_to=CVPage.models.user_directory_path, verbose_name='Photo du projet'),
        ),
    ]
