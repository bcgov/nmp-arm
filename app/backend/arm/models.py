from django.db import models

RATING_DISPLAY_TEXT = (
    ('Low', 'Low'),
    ('Low-Med', 'Low-Med'),
    ('Medium', 'Medium'),
    ('Med-High', 'Med-High'),
    ('High', 'High'),
    ('Extreme', 'Extreme'),
)

class FormField(models.Model):
    
    field_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.field_name, self.description)


class AnswerOptionMixin(models.Model):
    class Meta:
        abstract=True
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class ForageHeightOption(AnswerOptionMixin):

    value = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return "value:{0}, description:{1}, active:{2}".format(self.value, self.description, self.active)

class WaterTableDepthOption(AnswerOptionMixin):
    value = models.IntegerField()

class SoilTypeOption(AnswerOptionMixin):
    value = models.CharField(max_length=50)

class SoilMoistureOption(AnswerOptionMixin):
    value = models.IntegerField()

class ForageDensityOption(AnswerOptionMixin):
    value = models.IntegerField()

class SurfaceConditionOption(AnswerOptionMixin):
    value = models.CharField(max_length=50)
    
class ApplicationEquipmentOption(AnswerOptionMixin):
    value = models.CharField(max_length=50)

class CriticalAreaOption(AnswerOptionMixin):
    value = models.CharField(max_length=50)


class RiskCutoffSetting(models.Model):

    risk_level_name = models.CharField(max_length=4)
    display = models.CharField(max_length=11)
    minimum_score = models.IntegerField()
    maximum_score = models.IntegerField()
    message = models.TextField(max_length=500, default='add a message', blank=False, null=False)


class RiskRatingMixin(models.Model):
    class Meta:
        abstract=True

    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=True, null=True)
    show_stop_application = models.BooleanField(default=False)
    stop_application_message = models.TextField(max_length=500, blank=True, null=True)

class NumericRiskRatingMixin(RiskRatingMixin):
    class Meta:
        abstract=True

    range_minimum = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    range_maximum = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    def __str__(self):
        return "range_minimum:{0}, range_maximum:{1}, risk_value:{2}, risk_display_text:{3}, caution_message:{4}".format(self.range_minimum, self.range_maximum, self.risk_value, self.risk_display_text, self.caution_message)

class Preciptation24RiskRating(NumericRiskRatingMixin):
    pass

class Preciptation72RiskRating(NumericRiskRatingMixin):
    pass

class SoilMoistureRiskRating(NumericRiskRatingMixin):
    pass

class WaterTableRiskRating(NumericRiskRatingMixin):
    pass

class ForageDensityRiskRating(NumericRiskRatingMixin):
    pass

class ForageHeightRiskRating(NumericRiskRatingMixin):
    pass

class ApplicationRiskRating(RiskRatingMixin):

    applicator_name = models.CharField(max_length=50, blank=False, null=False)

class SoilTypeRiskRating(RiskRatingMixin):

    soil_type = models.CharField(max_length=10, blank=False, null=False)

class SurfaceConditionRiskRating(RiskRatingMixin):

    surface_condition = models.CharField(max_length=10, blank=False, null=False)

class CriticalAreaRiskRating(RiskRatingMixin):

    answer = models.CharField(max_length=10, blank=False, null=False)

class ManureSetbackDistanceRiskRating(RiskRatingMixin):

    distance_minimum = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0)
    distance_maximum = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0)