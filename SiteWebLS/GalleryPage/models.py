from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField('Nom de la photo', max_length=100)
    description = models.CharField('Description', max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='photos')
    date = models.DateField('Date de la prise de vue', auto_now_add=True)

    def __str__(self):
        return self.name