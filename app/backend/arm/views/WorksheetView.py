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
from arm.models import FieldDescription, ForageHeightOption, WaterTableDepthOption

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

    def GetFieldDescriptions(self):
        fieldList = FieldDescription.objects.all()

        fieldDescriptions = {}

        for field in fieldList:
            fieldDescriptions[field.field_name] = field.description

        return fieldDescriptions

    def get( self, request, *args, **kwargs ):

        fieldDescriptions = self.GetFieldDescriptions()

        data = {
                'page_name': 'ARM Worksheet',
                'FarmName_description': fieldDescriptions['FarmName'],
                'Main_description': fieldDescriptions['Main'],
                'ApplicationDate_description': fieldDescriptions['ApplicationDate'],
                'FieldName_description': fieldDescriptions['FieldName'],
                '24Preciptation_description': fieldDescriptions['24Preciptation'],
                '72Preciptation_description': fieldDescriptions['72Preciptation'],
                'SoilType_description': fieldDescriptions['SoilType'],
                'SoilMoisture_description': fieldDescriptions['SoilMoisture'],
                'WaterTableDepth_description': fieldDescriptions['WaterTableDepth'],
                'ForageDensity_description': fieldDescriptions['ForageDensity'],
                'ForageHeight_description': fieldDescriptions['ForageHeight'],
                'FieldSurfaceConditions_description': fieldDescriptions['FieldSurfaceConditions'],
                'ManureApplicationEquipment_description': fieldDescriptions['ManureApplicationEquipment'],
                'WaterbodyCriticalArea_description': fieldDescriptions['WaterbodyCriticalArea'],
                'ManureSetback_description': fieldDescriptions['ManureSetback'],
        }
        data['ForageHeightOptions'] = ForageHeightOption.objects.all().order_by('id')
        data['WaterTableDepthOptions'] = WaterTableDepthOption.objects.all().order_by('id')
        data.update( csrf( request ) )

        return render_to_response( self.template_name, data )



