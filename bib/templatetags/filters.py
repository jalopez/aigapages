from django import template
from django.template.defaultfilters import stringfilter
from subprocess import Popen, PIPE
import os

TAGS_PATH = os.path.realpath(os.path.dirname(__file__))
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
@stringfilter
def latexescape(tex):
    try:
        #import ipdb; ipdb.set_trace()
        script = os.path.join(TAGS_PATH, 'perl/texcape.pl')
        process = Popen(['perl', script], stdin=PIPE, stdout=PIPE)
        process.stdin.write(tex.encode('utf8'))
        process.stdin.close()
        return process.stdout.read()
    except:
        return tex


# vim:set ts=4 sw=4 et:
