from ArticlePage.models import Article, Theme
from django import template
import django
django.setup()


register = template.Library()


def getattribute(value, arg):
    return getattr(value, arg)


register.filter('getattribute', getattribute)


def publicationhandle(value, arg):
    choices = Article.publication.field.choices
    name = ""
    for choice in choices:
        if choice[0] == value:
            name = choice[1]
            break
    if arg == 'NO':
        return name
    number = Article.objects.filter(**{'publication': value}).count()
    return name + " : " + number.__str__()


register.filter('publihandle', publicationhandle)
