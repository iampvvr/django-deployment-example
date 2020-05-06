from django import template

register = template.Library()
@register.filter(name='cut')
def remove(value,arg):
    return value.replace(arg,'')

#register.filter('remove',remove)
