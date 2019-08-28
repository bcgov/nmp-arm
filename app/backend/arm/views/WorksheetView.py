#
#  django imports
#
from django.conf import settings
from django.forms import Form
from django.contrib import messages
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.urls import reverse
from django.template.loader import render_to_string
from decouple import config

#
#  sys imports
#
from datetime import datetime
import json
import uuid
import io
import requests
import logging
logger = logging.getLogger( __file__ )


#
#  app imports
#
from .PdfView import WorksheetData, PdfView

class WorksheetForm( Form ):

    def __init__( self, *args, **kwargs ):
        super( WorksheetForm, self ).__init__( *args, **kwargs )

    def clean( self ):
        cleaned_data = super( WorksheetForm, self ).clean()
        return cleaned_data


def format_submission( sdict ):

    worksheetData = WorksheetData(
        sdict.get( 'dairy_farm_name', '' ) ,
        sdict.get( 'apply_date', '' ) , 
        sdict.get( 'managment_unit', '' ) ,
        sdict.get( 'precipitation_1', '' ) ,
        sdict.get( 'precipitation_2', '' ) ,
        sdict.get( 'water_table_depth', '' ) ,
        sdict.get( 'forage_height', '' ) ,
        sdict.get( 'soil_type', '' ) ,
        sdict.get( 'soil_moisture', '' ) ,
        sdict.get( 'forage_density', '' ) ,
        sdict.get( 'application_equipment', '' ) ,
        sdict.get( 'critical_area', '' ) ,
        sdict.get( 'manure_setback_distance', '' ) ,
        sdict.get( 'surface_condition', '' ) ,)

    return worksheetData


def generate_pdf(worksheetData):

    # Rendered
    html_string = render_to_string('pdf.html', {'WorksheetData': worksheetData})
    weasy_server = ("%s/pdf?filename=arm_report.pdf" % config('WEASYPRINT_URL'))

    response = requests.post(weasy_server, data=html_string) 

    return response


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
        worksheetData = format_submission( self.request.POST )
        
        #return super( WorksheetView, self ).form_valid( form )
        # response = generate_pdf(worksheetData)
        # print(response.headers)
        
        html_string = render_to_string('pdf.html', {'WorksheetData': worksheetData})

        response = HttpResponse(content_type='text/html;')
        response.write(html_string)
        return response

    def post( self, request, *args, **kwargs ):

        logger.debug( "[ POST PARAMS ]: %s" % json.dumps( request.POST, indent=4 ) )

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            self.set_success_url()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


