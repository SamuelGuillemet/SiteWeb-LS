# Generated by Django 4.1 on 2023-01-14 00:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0009_alter_source_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
