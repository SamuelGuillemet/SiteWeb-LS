from django import template


register = template.Library()


def modulo(value, args):
    if(args == 'odd'):
        return (value % 2) == 1
    return (value % 2) == 0


register.filter('modulo', modulo)
