from CVPage.models import Social
from django import template
from django.utils import timezone
import django
django.setup()


register = template.Library()


def getattribute(value, arg):
    return getattr(value, arg)


register.filter('getattribute', getattribute)


def brand(value, arg):
    links = Social.nom.field.choices
    name = ""
    for link in links:
        if link[0] == arg:
            return value+link[1]


register.filter('brand', brand)


def age(value, arg):
    return (timezone.now().date() - value).days // 365


register.filter('age', age)
