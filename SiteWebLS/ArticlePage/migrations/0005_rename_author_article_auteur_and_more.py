# Generated by Django 4.0.3 on 2022-05-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0004_theme_etude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='Auteur',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='publication',
            new_name='Publication',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='Titre',
        ),
        migrations.AlterField(
            model_name='theme',
            name='Enfance',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='theme',
            name='Enquête',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='theme',
            name='Portrait',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='theme',
            name='Reportage',
            field=models.BooleanField(default=False),
        ),
    ]
