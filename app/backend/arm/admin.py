from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import FieldDescription, ForageHeightOption

@admin.register(FieldDescription)
class FieldDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'field_name', 'description')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':200})},
    }

@admin.register(ForageHeightOption)
class ForageHeightOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'description', 'active')