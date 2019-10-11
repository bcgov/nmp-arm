from django.test import TestCase

from arm.views import WorksheetView
from arm.models import FormField, ForageHeightOption, WaterTableDepthOption, \
                    ApplicationEquipmentOption, SoilTypeOption, CriticalAreaOption, \
                    SoilMoistureOption, ForageDensityOption, SurfaceConditionOption, RiskCutoffSetting, \
                    Preciptation24RiskRating, Preciptation72RiskRating, SoilMoistureRiskRating, ForageDensityRiskRating, ForageHeightRiskRating, \
                    ApplicationRiskRating, SoilTypeRiskRating, SurfaceConditionRiskRating, CriticalAreaRiskRating, \
                    ManureSetbackDistanceRiskRating, WaterTableRiskRating
import json

def is_json(json_string):
  try:
    json_object = json.loads(json_string)
  except ValueError as e:
    return False
  return True

class WorksheetViewTestCase(TestCase):
    fixtures = ["initial_data.json"]

    def test_static_data_is_complete(self):
        target = WorksheetView.StaticData()

        self.assertIsNotNone(target.application_date)
        self.assertIsNotNone(target.farm_name)
        self.assertIsNotNone(target.main)
        self.assertIsNotNone(target.field_name)
        self.assertIsNotNone(target.preciptation_24)
        self.assertIsNotNone(target.preciptation_72)
        self.assertIsNotNone(target.soil_type)
        self.assertIsNotNone(target.soil_moisture)
        self.assertIsNotNone(target.water_table_depth)
        self.assertIsNotNone(target.forage_density)
        self.assertIsNotNone(target.forage_height)
        self.assertIsNotNone(target.field_surface_conditions)
        self.assertIsNotNone(target.manure_application_equipment)
        self.assertIsNotNone(target.waterbody_critical_area)
        self.assertIsNotNone(target.manure_setback)

        self.assertGreater(len(target.soil_type_options), 0)
        self.assertGreater(len(target.soil_moisture_options), 0)
        self.assertGreater(len(target.forage_density_options), 0)
        self.assertGreater(len(target.surface_condition_options), 0)
        self.assertGreater(len(target.forage_height_options), 0)
        self.assertGreater(len(target.water_table_depth_options), 0)
        self.assertGreater(len(target.application_equipment_options), 0)
        self.assertGreater(len(target.critical_area_options), 0)

        self.assertGreater(len(target.fields_configurations), 0)
        self.assertGreater(len(target.risk_cuttoff_settings), 0)
        self.assertGreater(len(target.application_equipment_risk_settings), 0)
        self.assertGreater(len(target.soil_type_risk_settings), 0)
        self.assertGreater(len(target.surface_condition_risk_settings), 0)
        self.assertGreater(len(target.critical_area_risk_settings), 0)
        self.assertGreater(len(target.manure_setback_settings), 0)

        self.assertTrue(is_json(target.fields_configurations))
        self.assertTrue(is_json(target.risk_cuttoff_settings))
        self.assertTrue(is_json(target.application_equipment_risk_settings))
        self.assertTrue(is_json(target.soil_type_risk_settings))
        self.assertTrue(is_json(target.surface_condition_risk_settings))
        self.assertTrue(is_json(target.critical_area_risk_settings))
        self.assertTrue(is_json(target.manure_setback_settings))

