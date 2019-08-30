from django.db import models



class FieldDescription(models.Model):
    
    field_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.field_name, self.description)

    def GetFieldDescription(self, fieldname):
        return FieldDescription.objects.get(field_name=fieldname)

class ForageHeightOption(models.Model):

    value = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return "value:{0}, description:{1}, active:{2}".format(self.value, self.description, self.active)

class WaterTableDepthOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=50)
    active = models.BooleanField()
