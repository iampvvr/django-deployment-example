from django import template

register = template.Library()
@register.filter('namev')
def namev(value,arg):
    if(value == arg):
        return value
