# Generated by Django 4.1 on 2022-09-05 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CVPage', '0006_alter_social_link'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='experience',
            name='check_start_date',
        ),
    ]