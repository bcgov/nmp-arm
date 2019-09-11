from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import ApplicationEquipmentOption, FormField, ForageDensityOption, ForageHeightOption, SoilMoistureOption, SoilTypeOption, SurfaceConditionOption, WaterTableDepthOption, \
                    CautionMessage, RiskRatingValue, SurfaceConditionCautionMessage, RestrictionStopMessage

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

@admin.register(RiskRatingValue)
class RiskRatingValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_name', 'value_list')

@admin.register(CautionMessage)
class CautionMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_name', 'risk_caution_value', 'message')

@admin.register(SurfaceConditionCautionMessage)
class SurfaceConditionCautionMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_caution_value', 'message')

@admin.register(RestrictionStopMessage)
class RestrictionStopMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_name', 'stop_message')