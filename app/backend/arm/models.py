from django.db import models

class FormField(models.Model):
    
    field_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.field_name, self.description)


class ForageHeightOption(models.Model):

    value = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "value:{0}, description:{1}, active:{2}".format(self.value, self.description, self.active)

class WaterTableDepthOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

class SoilTypeOption(models.Model):

    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class SoilMoistureOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class ForageDensityOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class SurfaceConditionOption(models.Model):

    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    
class ApplicationEquipmentOption(models.Model):

    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)