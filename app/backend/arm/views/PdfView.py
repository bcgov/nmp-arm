from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.template.loader import render_to_string
from decouple import config

import requests
import tempfile

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
                    total_risk):

        self.farm_name = farm_name
        self.apply_date = apply_date
        self.managment_unit = managment_unit
        self.precipitation_1 = precipitation_1
        self.precipitation_1_risk = precipitation_1_risk
        self.precipitation_2 = precipitation_2
        self.precipitation_2_risk = precipitation_2
        self.water_table_depth = water_table_depth
        self.water_table_depth_risk = water_table_depth_risk
        self.forage_height = forage_height
        self.forage_height_risk = forage_height_risk
        self.soil_type = soil_type
        self.soil_moisture = soil_moisture
        self.soil_moisture_risk = soil_moisture_risk
        self.forage_density = forage_density
        self.forage_density_risk = forage_density_risk
        self.application_equipment = application_equipment
        self.application_equipment_risk = application_equipment_risk
        self.critical_area = critical_area
        self.critical_area_risk = critical_area_risk
        self.manure_setback_distance = manure_setback_distance
        self.manure_setback_distance_risk = manure_setback_distance_risk
        self.surface_condition = surface_condition
        self.surface_condition_risk = surface_condition_risk
        self.total_risk = total_risk

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
            sdict.get( 'total_risk', '' ) ,)
            
        return worksheetData

    def generate_pdf(self, worksheetData):

        # Rendered
        html_string = render_to_string('pdf.html', {'WorksheetData': worksheetData}).encode('utf-8')
        weasy_server = ("%s/pdf" % config('WEASYPRINT_URL'))

        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        result = requests.post(weasy_server, data=html_string, headers=headers) 
        # # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=arm_report.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        response.content = result.content

        return response

    def post( self, request ):

        data = self.format_submission(self.request.POST)
        response = self.generate_pdf(data)
        return response