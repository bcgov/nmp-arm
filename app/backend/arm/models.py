from django.db import models



class FieldDescription(models.Model):
    
    field_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.field_name, self.description)

    def GetFieldDescription(self, fieldname):
        return FieldDescription.objects.get(field_name=fieldname)
    