# Generated by Django 4.0.3 on 2022-05-02 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlePage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ArticlePage.article'),
        ),
    ]
