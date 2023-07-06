# Generated by Django 4.1 on 2023-01-14 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0010_alter_article_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='EF',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='EN',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='ET',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='PO',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='RE',
        ),
        migrations.AddField(
            model_name='theme',
            name='title',
            field=models.CharField(default=None, max_length=50, verbose_name='Titre'),
        ),
        migrations.RemoveField(
            model_name='theme',
            name='article',
        ),
        migrations.AddField(
            model_name='theme',
            name='article',
            field=models.ManyToManyField(blank=True, to='ArticlePage.article'),
        ),
    ]