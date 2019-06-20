from django import template
register = template.Library()

import logging
logger = logging.getLogger( __file__ )

@register.filter
def get_measure_freq_by_id( queryset, id_lookup ):
    logger.debug( "measure_id =  %s" % id_lookup )
    logger.debug( "queryset = %s" % queryset )
    client_measure = [ i for i in queryset if i.measure_id==id_lookup ]
    if client_measure:
        logger.debug( "got client measure = %s " % client_measure[0] )
        return client_measure[0].frequency_type.name
