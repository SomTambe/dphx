from django.db import models

class HX_setup(models.Model):
    Tcin_id = models.TextField(max_length=15)
    Tcout_id = models.TextField(max_length=15)
    Thin_id = models.TextField(max_length=15)
    Thout_id = models.TextField(max_length=15)
    Tsetpt_id = models.TextField(max_length=15)

class HX(models.Model):
    Tcin = models.FloatField(default=.0)
    Tcout = models.FloatField(default=.0)
    Thin = models.FloatField(default=.0)
    Thout = models.FloatField(default=.0)
    Fcold = models.FloatField(default=.0)
    Fhot = models.FloatField(default=.0)
    Tsetpt = models.FloatField(default=40.0)
