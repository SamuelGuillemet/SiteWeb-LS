from ArticlePage.models import Article, Theme
from django import template
import django
django.setup()


register = template.Library()


def getattribute(value, arg):
    return getattr(value, arg)


register.filter('getattribute', getattribute)


def themehandle(value, arg):
    name = Theme._meta.get_field(value).verbose_name
    number = Theme.objects.filter(**{value: True}).count()
    return name + " : " + number.__str__()


register.filter('themehandle', themehandle)


def publicationhandle(value, arg):
    choices = Article.publication.field.choices
    name = ""
    for choice in choices:
        if choice[0] == value:
            name = choice[1]
            break
    number = Article.objects.filter(**{'publication': value}).count()
    return name + " : " + number.__str__()


register.filter('publihandle', publicationhandle)
