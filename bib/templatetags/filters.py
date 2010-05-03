from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as escape

register = template.Library()

@register.filter
@stringfilter
def encode(value):     
    try:
        return unicode(value).encode('latin1').decode('utf8')
    except:
        return value
encode.is_safe=True

@register.filter
def author_cite(author, authors):
    if authors.has_key(author.author_id):
        return mark_safe('<a href="%s">%s</a>' % (escape(authors[author.author_id]), escape(encode(author.cleanname))))
    else:
        return encode(author.cleanname)
author_cite.is_safe=False

# vim:set ts=4 sw=4 et:
