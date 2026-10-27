from django import template
from django.template.defaultfilters import slugify
import logging
logger = logging.getLogger( __file__ )
register = template.Library()

@register.filter
def body_name( page_name ):
    return slugify( page_name )
