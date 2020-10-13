#
#  django imports
#
from django.conf import settings
from django.forms import Form
from django.contrib import messages
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.urls import reverse
from django.template.loader import render_to_string
from decouple import config

#
#  sys imports
#
from decimal import Decimal
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
from arm.models import FormField, ForageHeightOption, WaterTableDepthOption, \
                    ApplicationEquipmentOption, SoilTypeOption, CriticalAreaOption, \
                    SoilMoistureOption, ForageDensityOption, SurfaceConditionOption, RiskCutoffSetting, \
                    Preciptation24RiskRating, Preciptation72RiskRating, SoilMoistureRiskRating, ForageDensityRiskRating, ForageHeightRiskRating, \
                    ApplicationRiskRating, SoilTypeRiskRating, SurfaceConditionRiskRating, CriticalAreaRiskRating, \
                    ManureSetbackDistanceRiskRating, WaterTableRiskRating

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

        return render( None, self.template_name, data )


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

        self.soil_type_options = SoilTypeOption.objects.filter(active=True).order_by('id')
        self.soil_moisture_options = SoilMoistureOption.objects.filter(active=True).order_by('id')
        self.forage_density_options = ForageDensityOption.objects.filter(active=True).order_by('id')
        self.surface_condition_options = SurfaceConditionOption.objects.filter(active=True).order_by('id')
        self.forage_height_options = ForageHeightOption.objects.filter(active=True).order_by('id')
        self.water_table_depth_options = WaterTableDepthOption.objects.filter(active=True).order_by('id')
        self.application_equipment_options = ApplicationEquipmentOption.objects.filter(active=True).order_by('id')
        self.critical_area_options = CriticalAreaOption.objects.filter(active=True).order_by('id')

        self.fields_configurations = fields_configurations().toJSON()
        self.risk_cuttoff_settings = risk_cuttoff_settings().toJSON()
        self.application_equipment_risk_settings = application_equipment_risk_settings().toJSON()
        self.soil_type_risk_settings = soil_type_risk_settings().toJSON()
        self.surface_condition_risk_settings = surface_condition_risk_settings().toJSON()
        self.critical_area_risk_settings = critical_area_risk_settings().toJSON()
        self.manure_setback_settings = manure_setback_settings().toJSON()

class JSONSerializable():
    
    def _try(self, o): 

        if isinstance(o, Decimal):
            return float(o)
    
        try: 
            return o.__dict__ 
        except TypeError:
            pass
        else:
            return str(o).__dict__ 

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, o)

    def toJSON(self): 
        return json.dumps(self, default=lambda o: self._try(o), sort_keys=False, indent=0, separators=(',',':')).replace('\n', '')

class fields_configurations(JSONSerializable):

    def __init__(self):
        self.precipitation_1 = field('24precipitation')
        self.precipitation_2 = field('72precipitation')
        self.soil_moisture = field('soil_moisture')
        self.water_table_depth = field('water_table_depth')
        self.forage_density = field('forage_density')
        self.forage_height = field('forage_height')
        self.surface_condition = field('surface_condition')
        self.soil_type = field('soil_type')
        self.application_equipment = field('application_equipment')
        self.critical_area = field('critical_area')
        self.manure_setback_distance = field('manure_setback_distance')

class field():   

    def __init__(self, field_name):
        self.trigger = 'input change keyup'
        self.validators = validator(field_name)

class validator():

    def __init__(self, field_name):

        if field_name == '24precipitation':
            self.risk_rating = preciptation_24_risk_settings()
        elif field_name == '72precipitation':
            self.risk_rating = preciptation_72_risk_settings()
        elif field_name == 'soil_type':
            self.soil_type_risk_rating = soil_type_risk_rating()
        elif field_name == 'soil_moisture':
            self.risk_rating = soil_moisture_risk_settings()
        elif field_name == 'water_table_depth':
            self.risk_rating = water_table_depth_risk_settings()
        elif field_name == 'forage_height':
            self.risk_rating = forage_height_risk_settings()
        elif field_name == 'forage_density':
            self.risk_rating = forage_density_risk_settings()
        elif field_name == 'application_equipment':
            self.applicator_risk_rating = applicator_risk_rating()
        elif field_name == 'critical_area':
            self.show_hide = show_hide()
            self.critical_area_risk_rating = critical_area_risk_rating()
        elif field_name == 'manure_setback_distance':
            self.manure_setback_distance = manure_setback_distance()
        elif field_name == 'surface_condition':
            self.surface_risk_rating = surface_risk_rating()  

class surface_risk_rating():

    def __init__(self):
        self.comparitor = 'in'
        self.stop_values = {'flooding': True, 'frozen': True, 'snow-ice': True}

class soil_type_risk_rating():
    pass
    
class applicator_risk_rating():
    pass
    
class critical_area_risk_rating():
    pass

class show_hide():
    pass

class manure_setback_distance():
    pass

class risk_cuttoff_settings(JSONSerializable):

    def __init__(self):
        self.low = risk_cuttoff('low')
        self.med = risk_cuttoff('med')
        self.high = risk_cuttoff('high')

class risk_cuttoff():

    def __init__(self, level):
        setting = RiskCutoffSetting.objects.get(risk_level_name__exact=level)
        self.display = setting.display
        self.minimum_score = setting.minimum_score
        self.maximum_score = setting.maximum_score
        self.message = setting.message

class risk_setting(JSONSerializable):
    def load_setting(self, settings_name, settings):
        
        for setting in settings:
            self.__dict__[setting.pk] = risk_rating_setting(setting)
            self.__dict__[setting.pk].range_minimum = setting.range_minimum
            self.__dict__[setting.pk].range_maximum = setting.range_maximum

class preciptation_24_risk_settings(risk_setting):
    def __init__(self):
        settings = Preciptation24RiskRating.objects.all()
        self = self.load_setting('precipitation_1', settings)

class preciptation_72_risk_settings(risk_setting):
    def __init__(self):
        settings = Preciptation72RiskRating.objects.all()
        self = self.load_setting('precipitation_2', settings)

class soil_type_risk_settings(risk_setting):
    def __init__(self):
        settings = SoilTypeRiskRating.objects.all()
        self = self.load_setting('soil_type', settings)

class soil_moisture_risk_settings(risk_setting):
    def __init__(self):
        settings = SoilMoistureRiskRating.objects.all()
        self = self.load_setting('soil_moisture', settings)

class water_table_depth_risk_settings(risk_setting):
    def __init__(self):
        settings = WaterTableRiskRating.objects.all()
        self.values = self.load_setting('water_table_depth', settings)

class forage_density_risk_settings(risk_setting):
    def __init__(self):
        settings = ForageDensityRiskRating.objects.all()
        self = self.load_setting('forage_density', settings)

class forage_height_risk_settings(risk_setting):
    def __init__(self):
        settings = ForageHeightRiskRating.objects.all()
        self = self.load_setting('forage_height', settings)

class application_equipment_risk_settings(JSONSerializable):
    
    def __init__(self):
        settings = ApplicationRiskRating.objects.all().order_by('id')

        for setting in settings:
            saved_setting = risk_rating_setting(setting)
            self.__dict__[setting.applicator_name] = saved_setting     

class soil_type_risk_settings(JSONSerializable):
    
    def __init__(self):
        settings = SoilTypeRiskRating.objects.all().order_by('id')

        for setting in settings:
            saved_setting = risk_rating_setting(setting)
            self.__dict__[setting.soil_type] = saved_setting     

class surface_condition_risk_settings(JSONSerializable):
    
    def __init__(self):
        settings = SurfaceConditionRiskRating.objects.all().order_by('id')

        for setting in settings:
            saved_setting = risk_rating_setting(setting)
            self.__dict__[setting.surface_condition] = saved_setting     


class critical_area_risk_settings(JSONSerializable):
    
    def __init__(self):
        settings = CriticalAreaRiskRating.objects.all().order_by('id')

        for setting in settings:
            saved_setting = risk_rating_setting(setting)
            self.__dict__[setting.answer] = saved_setting     

class manure_setback_settings(JSONSerializable):
    
    def __init__(self):
        settings = ManureSetbackDistanceRiskRating.objects.all().order_by('id')
        for setting in settings:
            self.__dict__[setting.pk] = risk_rating_setting(setting)
            self.__dict__[setting.pk].distance_minimum = setting.distance_minimum     
            self.__dict__[setting.pk].distance_maximum = setting.distance_maximum     

class risk_rating_setting():

    def __init__(self, risk_rating):
        self.risk_value = risk_rating.risk_value
        self.risk_display_text = risk_rating.risk_display_text
        try:
            self.caution_message = risk_rating.caution_message
        except:
            self.caution_message = ''

        try:
            self.show_stop_application = risk_rating.show_stop_application
        except:
            self.show_stop_application = False

        try:
            self.stop_application_message = risk_rating.stop_application_message
        except:
            self.stop_application_message = False
