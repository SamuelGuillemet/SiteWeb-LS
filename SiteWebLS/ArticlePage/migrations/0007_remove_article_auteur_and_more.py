# Generated by Django 4.0.3 on 2022-05-02 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0006_alter_theme_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Auteur',
        ),
        migrations.RemoveField(
            model_name='article',
            name='Date de publication',
        ),
        migrations.RemoveField(
            model_name='article',
            name='Publication',
        ),
        migrations.RemoveField(
            model_name='article',
            name='Titre',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='Enfance',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='Enquête',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='Etude',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='Portrait',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='Reportage',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=None, max_length=50, verbose_name='Auteur'),
        ),
        migrations.AddField(
            model_name='article',
            name='publication',
            field=models.CharField(choices=[('SP', 'Sciences Po'), ('ML', 'La manche libre')], default='SP', max_length=2, verbose_name='Publication'),
        ),
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date de publication'),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default=None, max_length=150, verbose_name='Titre'),
        ),
        migrations.AddField(
            model_name='theme',
            name='EF',
            field=models.BooleanField(default=False, verbose_name='Enfance'),
        ),
        migrations.AddField(
            model_name='theme',
            name='EN',
            field=models.BooleanField(default=False, verbose_name='Enquête'),
        ),
        migrations.AddField(
            model_name='theme',
            name='ET',
            field=models.BooleanField(default=False, verbose_name='Etude'),
        ),
        migrations.AddField(
            model_name='theme',
            name='PO',
            field=models.BooleanField(default=False, verbose_name='Portrait'),
        ),
        migrations.AddField(
            model_name='theme',
            name='RE',
            field=models.BooleanField(default=False, verbose_name='Reportage'),
        ),
    ]