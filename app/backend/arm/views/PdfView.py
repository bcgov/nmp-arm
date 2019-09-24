from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from decouple import config

import requests
import tempfile

from arm.models import FormField, ForageHeightOption, WaterTableDepthOption, RiskRatingValue, CautionMessage, \
                    RestrictionStopMessage, ApplicationEquipmentOption, SoilTypeOption, \
                    SoilMoistureOption, ForageDensityOption, SurfaceConditionOption

class WorksheetData:
    def __init__(self, farm_name,
                    apply_date,
                    managment_unit,
                    precipitation_1,
                    precipitation_1_risk,
                    precipitation_2,
                    precipitation_2_risk,
                    water_table_depth,
                    water_table_depth_risk,
                    forage_height,
                    forage_height_risk,
                    soil_type,
                    soil_moisture,
                    soil_moisture_risk,
                    forage_density,
                    forage_density_risk,
                    application_equipment,
                    application_equipment_risk,
                    critical_area,
                    critical_area_risk,
                    manure_setback_distance,
                    manure_setback_distance_risk,
                    surface_condition,
                    surface_condition_risk,
                    total_risk,
                    emailAddressForReport):

        self.farm_name = farm_name
        self.apply_date = apply_date
        self.managment_unit = managment_unit
        self.precipitation_1 = precipitation_1
        self.precipitation_1_risk = precipitation_1_risk
        self.precipitation_2 = precipitation_2
        self.precipitation_2_risk = precipitation_2_risk
        self.water_table_depth = water_table_depth
        self.water_table_depth_risk = water_table_depth_risk
        self.forage_height = forage_height
        self.forage_height_risk = forage_height_risk
        self.soil_type = soil_type
        self.soil_moisture = int(soil_moisture)
        self.soil_moisture_risk = soil_moisture_risk
        self.forage_density = int(forage_density)
        self.forage_density_risk = forage_density_risk
        self.application_equipment = application_equipment
        self.application_equipment_risk = application_equipment_risk
        self.critical_area = critical_area.upper()
        self.critical_area_risk = critical_area_risk
        self.manure_setback_distance = manure_setback_distance
        self.manure_setback_distance_risk = manure_setback_distance_risk
        self.surface_condition = surface_condition
        self.surface_condition_risk = surface_condition_risk
        self.total_risk = total_risk
        self.emailAddressForReport = emailAddressForReport

        fieldList = FormField.objects.all()

        form_fields = {}

        for field in fieldList:
            form_fields[field.field_name] = field

        self.application_date_field = form_fields['ApplicationDate']
        self.farm_name_field = form_fields['FarmName']
        self.main_field = form_fields['Main']
        self.field_name = form_fields['FieldName']
        self.preciptation_24_field = form_fields['24Preciptation']
        self.preciptation_72_field = form_fields['72Preciptation']
        self.soil_type_field = form_fields['SoilType']
        self.soil_moisture_field = form_fields['SoilMoisture']
        self.water_table_depth_field = form_fields['WaterTableDepth']
        self.forage_density_field = form_fields['ForageDensity']
        self.forage_height_field = form_fields['ForageHeight']
        self.field_surface_conditions_field = form_fields['FieldSurfaceConditions']
        self.manure_application_equipment_field = form_fields['ManureApplicationEquipment']
        self.waterbody_critical_area_field = form_fields['WaterbodyCriticalArea']
        self.manure_setback_field = form_fields['ManureSetback']

        self.soil_type_options = SoilTypeOption.objects.filter(active=True).order_by('id')
        self.soil_moisture_options = SoilMoistureOption.objects.filter(active=True).order_by('id')
        self.forage_density_options = ForageDensityOption.objects.filter(active=True).order_by('id')
        self.surface_condition_options = SurfaceConditionOption.objects.filter(active=True).order_by('id')
        self.forage_height_options = ForageHeightOption.objects.filter(active=True).order_by('id')
        self.water_table_depth_options = WaterTableDepthOption.objects.filter(active=True).order_by('id')
        self.application_equipment_options = ApplicationEquipmentOption.objects.filter(active=True).order_by('id')

class PdfView(FormView):
    template_name = 'pdf.html'
    form_class = WorksheetData 

    http_method_names = [ 'post' ]

    def format_submission(self, sdict ):
        worksheetData = WorksheetData(
            sdict.get( 'dairy_farm_name', '' ) ,
            sdict.get( 'apply_date', '' ) , 
            sdict.get( 'managment_unit', '' ) ,
            sdict.get( 'precipitation_1', '' ) ,
            sdict.get( 'precipitation_1_risk', 'N/A' ) ,
            sdict.get( 'precipitation_2', '' ) ,
            sdict.get( 'precipitation_2_risk', 'N/A' ) ,
            sdict.get( 'water_table_depth', '' ) ,
            sdict.get( 'water_table_depth_risk', 'N/A' ) ,
            sdict.get( 'forage_height', '' ) ,
            sdict.get( 'forage_height_risk', 'N/A' ) ,
            sdict.get( 'soil_type', '' ) ,
            sdict.get( 'soil_moisture', '' ) ,
            sdict.get( 'soil_moisture_risk', 'N/A' ) ,
            sdict.get( 'forage_density', '' ) ,
            sdict.get( 'forage_density_risk', 'N/A' ) ,
            sdict.get( 'application_equipment', '' ) ,
            sdict.get( 'application_equipment_risk', 'N/A' ) ,
            sdict.get( 'critical_area', '' ) ,
            sdict.get( 'critical_area_risk', 'N/A' ) ,
            sdict.get( 'manure_setback_distance', '' ) ,
            sdict.get( 'manure_setback_distance_risk', 'N/A' ) ,
            sdict.get( 'surface_condition_list', '' ) ,
            sdict.get( 'surface_condition_risk', 'N/A' ) ,
            sdict.get( 'total_risk', '' ) ,
            sdict.get( 'emailAddressForReport', '' ),)
            
        return worksheetData

    def generate_pdf(self, worksheetData):

        # Rendered
        html_string = render_to_string('pdf.html', {'WorksheetData': worksheetData}).encode('utf-8')
        weasy_server = ("%s/pdf" % config('WEASYPRINT_URL'))

        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        
        try:
            response = HttpResponse(content_type='application/pdf;')
            result = requests.post(weasy_server, data=html_string, headers=headers) 
            # # Creating http response
            response['Content-Disposition'] = 'inline; filename=arm_report.pdf'
            response['Content-Transfer-Encoding'] = 'binary'
            response.content = result.content

        except Exception as e:
            print(e)
            logger.exception( e )
            response.status_code = 500
            response.content = 'PDF generation failed'

        return response

    def get_pdf_response(self, worksheetData):

        pdfResult = self.generate_pdf(worksheetData)

        # # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=arm_report.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        response.content = pdfResult.content

        return response

    def email_pdf(self, worksheetData):
 
        pdfResult = self.generate_pdf(worksheetData)
        response = HttpResponse(content_type='text/html;')

        if pdfResult.status_code == requests.codes.ok:

            filename = ("%s.pdf" % worksheetData.farm_name).replace(" ", "")
            try:
                email = EmailMessage(
                            'ARM worksheet submission',
                            'please see attachement',
                            config('DEFAULT_FROM_EMAIL'),
                            [worksheetData.emailAddressForReport],
                            headers = {})
                email.attach(filename, pdfResult.content,'application/pdf')
                email.send()
                response.status_code = 200

            except Exception as e:
                print(e)
                logger.exception( e )
                response.status_code = 500
                response.content = 'Email failed'
        else:
            response.status_code = pdfResult.status_code

        return response


    def post( self, request ):
        reporttype = request.POST.get("reportType", None)
        data = self.format_submission(self.request.POST)
        if reporttype == 'email':
            response = self.email_pdf(data)
        else:
            response = self.generate_pdf(data)
        return response