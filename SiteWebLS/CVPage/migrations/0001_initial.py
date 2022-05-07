# Generated by Django 4.0.3 on 2022-05-07 00:11

import CVPage.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom de famille')),
                ('prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('birth_date', models.DateField(default=datetime.date(2000, 1, 1), verbose_name='Date de naissance')),
                ('mail', models.CharField(max_length=50, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='Numéro de téléphone')),
                ('speech', models.TextField(verbose_name='Présentation rapide')),
                ('photo', models.ImageField(upload_to=CVPage.models.user_directory_path, verbose_name='Photo de profil')),
                ('statut', models.CharField(max_length=50, verbose_name='Statut actuel')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('GH', 'Github'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('FB', 'Facebook'), ('LN', 'LinkenIn')], max_length=2, verbose_name='Nom du réseau')),
                ('link', models.CharField(max_length=50, null=True, verbose_name='Lien du réseau')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVPage.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom de la compétence')),
                ('percentage', models.PositiveIntegerField(verbose_name='Pourcentage de maitrise de la compétence')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVPage.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du projet')),
                ('link', models.CharField(max_length=50, null=True, verbose_name='Lien vers le projet')),
                ('photo', models.ImageField(upload_to=CVPage.models.user_directory_path, verbose_name='Photo de profil')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVPage.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, verbose_name="Role dans l'expérience")),
                ('entreprise', models.CharField(max_length=50, null=True, verbose_name="Nom de l'entreprise")),
                ('date_debut', models.DateField(verbose_name='Date de début')),
                ('date_fin', models.DateField(verbose_name='Date de fin')),
                ('description', models.TextField(verbose_name="Description de l'expérience")),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVPage.cv')),
            ],
        ),
        migrations.AddConstraint(
            model_name='skills',
            constraint=models.CheckConstraint(check=models.Q(('percentage__lte', 100)), name='percentage__lte_100'),
        ),
        migrations.AddConstraint(
            model_name='experiences',
            constraint=models.CheckConstraint(check=models.Q(('date_fin__gte', django.db.models.expressions.F('date_debut'))), name='check_start_date'),
        ),
    ]
