from django.db import models
from django.db.models import CheckConstraint, Q, F
import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.pk, filename)


def make_file_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.cv.pk, filename)


# Create your models here.


class CV(models.Model):
    nom = models.CharField('Nom de famille', max_length=50)
    prenom = models.CharField('Prénom', max_length=50)
    birth_date = models.DateField(
        'Date de naissance', default=datetime.date.fromisoformat('2000-01-01'))
    mail = models.EmailField('Email', max_length=254)
    phone = models.CharField('Numéro de téléphone', max_length=50)
    speech = models.TextField('Présentation rapide')
    photo = models.ImageField(
        'Photo de profil', upload_to=user_directory_path, max_length=100)
    statut = models.CharField("Statut actuel", max_length=50)

    def __str__(self):
        return 'CV de ' + self.nom + " " + self.prenom

    def get_absolute_url(self):
        return reverse("CVPage:detail", kwargs={"id": self.pk})


class Skill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    nom = models.CharField("Nom de la compétence", max_length=50)
    percentage = models.PositiveIntegerField(
        "Pourcentage de maitrise de la compétence")

    def __str__(self):
        return 'Compétence en ' + self.nom

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(percentage__lte=100),
                name='percentage__lte_100')
        ]

    def clean(self):
        if self.percentage is not None:
            if self.percentage > 100:
                raise ValidationError(
                    {'percentage': "Le pourcentage doit être en dessous de 100%"})


class Project(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    nom = models.CharField("Nom du projet", max_length=100)
    link = models.URLField("Lien vers le projet",
                           max_length=100, null=True, blank=True)
    photo = models.ImageField(
        'Photo du projet', upload_to=make_file_path, max_length=100)

    def __str__(self):
        return 'Projet de ' + self.nom


class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    role = models.CharField("Role dans l'expérience", max_length=50)
    entreprise = models.CharField(
        "Nom de l'entreprise", max_length=50, null=True, blank=True)
    date_debut = models.DateField("Date de début")
    date_fin = models.DateField("Date de fin", null=True, blank=True)
    description = models.TextField("Description de l'expérience")

    def __str__(self):
        return 'Expérience en tant que ' + self.role

    def clean(self):
        if (self.date_debut is not None) and (self.date_fin is not None):
            if self.date_debut > self.date_fin:
                raise ValidationError(
                    {'date_fin': 'La date de fin doit être plus grande que la date de début',
                     'date_debut': 'La date de début doit être plus petite que la date de fin'})


class Social(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    NOM_CHOICES = [
        ('GH', 'github'),
        ('TW', 'twitter'),
        ('IN', 'instagram'),
        ('FB', 'facebook'),
        ('LN', 'linkedin')
    ]

    nom = models.CharField(
        "Nom du réseau", max_length=2, choices=NOM_CHOICES)
    link = models.URLField(
        "Lien du réseau", max_length=100, default=None)

    def __str__(self):
        return self.nom
