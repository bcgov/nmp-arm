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
from arm.models import FormField, ForageHeightOption, WaterTableDepthOption

class WorksheetForm( Form ):

    def __init__( self, *args, **kwargs ):
        super( WorksheetForm, self ).__init__( *args, **kwargs )

    def clean( self ):
        cleaned_data = super( WorksheetForm, self ).clean()
        return cleaned_data

class WorksheetView( FormView ):

    template_name = 'worksheet.html'
    form_class = WorksheetForm 

    http_method_names = [ 'get', ]


    def get( self, request, *args, **kwargs ):

        staticData = StaticData()

        data = {
                'page_name': 'ARM Worksheet',
                'staticData': staticData
        }
        data.update( csrf( request ) )

        return render_to_response( self.template_name, data )


class StaticData():

    def __init__(self):

        fieldList = FormField.objects.all()

        form_fields = {}

        for field in fieldList:
            form_fields[field.field_name] = field

        self.application_date = form_fields['ApplicationDate']
        self.farm_name = form_fields['FarmName']
        self.main = form_fields['Main']
        self.field_name = form_fields['FieldName']
        self.preciptation_24 = form_fields['24Preciptation']
        self.preciptation_72 = form_fields['72Preciptation']
        self.soil_type = form_fields['SoilType']
        self.soil_moisture = form_fields['SoilMoisture']
        self.water_table_depth = form_fields['WaterTableDepth']
        self.forage_density = form_fields['ForageDensity']
        self.forage_height = form_fields['ForageHeight']
        self.field_surface_conditions = form_fields['FieldSurfaceConditions']
        self.manure_application_equipment = form_fields['ManureApplicationEquipment']
        self.waterbody_critical_area = form_fields['WaterbodyCriticalArea']
        self.manure_setback = form_fields['ManureSetback']

        self.forage_height_options = ForageHeightOption.objects.all().order_by('id')
        self.water_table_depth_options = WaterTableDepthOption.objects.all().order_by('id')


    def __str__(self):
        return self.farm_name.field_name
