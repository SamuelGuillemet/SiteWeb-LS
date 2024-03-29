# Generated by Django 4.1 on 2022-08-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom de la photo')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='photos')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date de la prise de vue')),
            ],
        ),
    ]
