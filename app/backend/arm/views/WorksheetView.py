#
#  django imports
#
from django.conf import settings
from django.forms import Form
from django.contrib import messages
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.urls import reverse


#
#  sys imports
#
from datetime import datetime
import json
import uuid
import io
import logging
logger = logging.getLogger( __file__ )


#
#  app imports
#
from common.functions.filesystem import create_dirs


class WorksheetForm( Form ):

    def __init__( self, *args, **kwargs ):
        super( WorksheetForm, self ).__init__( *args, **kwargs )

    def clean( self ):
        cleaned_data = super( WorksheetForm, self ).clean()
        return cleaned_data


def format_submission( sdict ):
    record = {}
    record[ 'headers' ] = [ 
        'Timestamp' ,
        'Farm_Name' ,
        'Apply_Date' ,
        'Field_Unit' ,
        '24_Precip' ,
        '24_Precip_Risk' ,
        '72_Precip' ,
        '72_Precip_Risk' ,
        'Soil_Type' ,
        'Soil_Mois' ,
        'Soil_Mois_Risk' ,
        'WaterT_Depth' ,
        'WaterT_Depth_Risk' ,
        'Forage_Density' ,
        'Forage_Density_Risk' ,
        'Forage_Height' ,
        'Forage_Height_Risk' ,
        'Surface_Condition' ,
        'Surface_Condition_Risk' ,
        'App_Equipment' ,
        'App_Equipment_Risk' ,
        'Critical_Area' ,
        'Manure_Setback' ,
        'Vegitative_Buffer' ,
        'Vegitative_Buffer_Risk' ,
        'Total_Risk' ,
    ]

    record[ 'row' ] = [
        datetime.now().strftime( '%m/%d/%y' ) ,
        sdict.get( 'dairy_farm_name', '' ) ,
        sdict.get( 'apply_date', '' ) , 
        sdict.get( 'managment_unit', '' ) ,
        sdict.get( 'precipitation_1', '' ) ,
        sdict.get( 'precipitation_1_risk', '' ) ,
        sdict.get( 'precipitation_2', '' ) ,
        sdict.get( 'precipitation_2_risk', '' ) ,
        sdict.get( 'soil_type', '' ) ,
        sdict.get( 'soil_moisture', '' ) ,
        sdict.get( 'soil_moisture_risk', '' ) ,
        sdict.get( 'water_table_depth', '' ) ,
        sdict.get( 'water_table_depth_risk', '' ) ,
        sdict.get( 'forage_density', '' ) ,
        sdict.get( 'forage_density_risk', '' ) ,
        sdict.get( 'forage_height', '' ) ,
        sdict.get( 'forage_height_risk', '' ) ,
        sdict.get( 'surface_condition', '' ) ,
        sdict.get( 'surface_condition_risk', '' ) ,
        sdict.get( 'application_equipment', '' ) ,
        sdict.get( 'application_equipment_risk', '' ) ,
        sdict.get( 'critical_area', '' ) ,
        sdict.get( 'manure_setback_distance', '' ) ,
        sdict.get( 'vegetation_buffer', '' ) ,
        sdict.get( 'vegetation_buffer_risk', '' ) ,
        sdict.get( 'total_risk', '' ) ,
    ]

    return record



class WorksheetView( FormView ):

    template_name = 'worksheet.html'
    form_class = WorksheetForm 

    http_method_names = [ 'get', 'post', ]

    def get( self, request, *args, **kwargs ):

        data = {
                'page_name': 'ARM Worksheet',
        }
        data.update( csrf( request ) )

        return render_to_response( self.template_name, data )

    def set_success_url( self ):
        self.success_url = reverse( 'thankyou', )

    def form_valid( self, form ):

        filename = 'submission-'+str(uuid.uuid4())+'.csv'
        logger.debug( "[ WRITING FILE ]: %s" % filename )
        with open( '/tmp/'+filename, 'w' ) as fsock:
            format = format_submission( self.request.POST )
            fsock.write( ','.join( format[ 'headers' ] ) + "\n" )
            fsock.write( ','.join( format[ 'row' ] ) + "\n" )

        try:
            email = EmailMessage(
                        'ARM worksheet submission', 
                        'please see attachement', 
                        'no_reply@whatcomcd.org',
                        ['NEmbertson@whatcomcd.org'], ['gregcorradini@gmail.com','whatcomcd6975@gmail.com'],
                        headers = {})
            email.attach_file('/tmp/'+filename)
            email.send()
        except Exception as e:
            logger.exception( e )
        return super( WorksheetView, self ).form_valid( form )

    def post( self, request, *args, **kwargs ):

        logger.debug( "[ POST PARAMS ]: %s" % json.dumps( request.POST, indent=4 ) )

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            self.set_success_url()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


