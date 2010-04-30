from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def encode(value):     
    return unicode(value).encode('latin1').decode('utf8')
encode.is_safe=True


# vim:set ts=4 sw=4 et:
