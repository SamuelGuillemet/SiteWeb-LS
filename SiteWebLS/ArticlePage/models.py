import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Article(models.Model):

    PUBLICATION_CHOICES = [
        ('SP', 'Sciences Po'),
        ('ML', 'La manche libre'),
    ]

    source_template = "1 - : \n2 - : \n3 - : \n4 - : \n..."

    title = models.CharField('Titre', max_length=150, default=None)
    author = models.CharField('Auteur', max_length=50, default=None)
    article = models.TextField(default=None)
    source = models.TextField(default=source_template)
    published_date = models.DateField('Date de publication',
                                      default=datetime.date.today)
    publication = models.CharField(
        'Publication', max_length=2, choices=PUBLICATION_CHOICES, default='SP')

    @admin.display(
        boolean=True,
        ordering='published_date',
        description='Publié récemment ?',
    )
    def was_published_recently(self):
        now = timezone.now().month
        return now - 3 <= self.published_date.month <= now

    def __str__(self):
        return self.title


class Theme(models.Model):
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, default=None)
    EF = models.BooleanField('Enfance', default=False)
    PO = models.BooleanField('Portrait', default=False)
    RE = models.BooleanField('Reportage', default=False)
    EN = models.BooleanField('Enquête', default=False)
    ET = models.BooleanField('Etude', default=False)

    def __str__(self):
        return "Themes de l'article : {}".format(self.article)
