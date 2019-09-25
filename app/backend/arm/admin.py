from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import ApplicationEquipmentOption, FormField, ForageDensityOption, ForageHeightOption, SoilMoistureOption, SoilTypeOption, \
                    SurfaceConditionOption, WaterTableDepthOption, RestrictionStopMessage, RiskCutoffSetting, \
                    Preciptation24RiskRating, Preciptation72RiskRating, SoilMoistureRiskRating, \
                    WaterTableRiskRating, ForageDensityRiskRating, ForageHeightRiskRating, \
                    ApplicationRiskRating, SoilTypeRiskRating, SurfaceConditionRiskRating, \
                    CriticalAreaRiskRating, ManureSetbackDistanceRiskRating

@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'field_name', 'title', 'description')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':200})},
    }
    

@admin.register(ApplicationEquipmentOption)
class ApplicationEquipmentOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')    

@admin.register(ForageDensityOption)
class ForageDensityOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')

@admin.register(ForageHeightOption)
class ForageHeightOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')

@admin.register(SoilMoistureOption)
class SoilMoistureOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')

@admin.register(SoilTypeOption)
class SoilTypeOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')

@admin.register(SurfaceConditionOption)
class SurfaceConditionOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')

@admin.register(WaterTableDepthOption)
class WaterTableDepthOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')

@admin.register(RestrictionStopMessage)
class RestrictionStopMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_name', 'stop_message')

@admin.register(RiskCutoffSetting)
class RiskCutoffSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_level_name', 'display', 'minimum_score', 'maximum_score', 'message')

@admin.register(Preciptation24RiskRating)
class Preciptation24RiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'range_minimum', 'range_maximum', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(Preciptation72RiskRating)
class Preciptation72RiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'range_minimum', 'range_maximum', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(SoilMoistureRiskRating)
class SoilMoistureRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'range_minimum', 'range_maximum', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(WaterTableRiskRating)
class WaterTableRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'range_minimum', 'range_maximum', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(ForageDensityRiskRating)
class ForageDensityRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'range_minimum', 'range_maximum', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(ForageHeightRiskRating)
class ForageHeightRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'range_minimum', 'range_maximum', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(ApplicationRiskRating)
class ApplicationRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'applicator_name', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(SoilTypeRiskRating)
class SoilTypeRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'soil_type', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(SurfaceConditionRiskRating)
class SurfaceConditionRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'surface_condition', 'is_a_stop_application_item', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(CriticalAreaRiskRating)
class CriticalAreaRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'risk_value', 'risk_display_text', 'caution_message')

@admin.register(ManureSetbackDistanceRiskRating)
class ManureSetbackDistanceRiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'distance_minimum', 'distance_maximum', 'risk_value', 'risk_display_text', 'caution_message')