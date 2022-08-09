from django.db import models

# Create your models here.


def directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'podcasts/{0}'.format(filename)


class Podcast(models.Model):
    title = models.CharField("Titre", max_length=50)
    author = models.CharField("Auteur", max_length=50)

    audio = models.FileField("Fichier du podcast",
                             upload_to=directory_path, max_length=100)

    def __str__(self):
        return self.title


class Theme(models.Model):
    podcast = models.OneToOneField(
        Podcast, on_delete=models.CASCADE)
    PO = models.BooleanField('Portrait')
    RE = models.BooleanField('Reportage')
    ET = models.BooleanField('Etude')
    MT = models.BooleanField('Micro trottoir')
    DI = models.BooleanField('Discussion')

    def __str__(self):
        return "Themes du podcast : {}".format(self.podcast)


class Chapitre(models.Model):
    podcast = models.ForeignKey(
        Podcast, on_delete=models.CASCADE)
    nom = models.CharField("Titre du chapitre", max_length=50)
    timestamp = models.TimeField(
        "Début du chapitre à", auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'Chapitre {self.nom}'
