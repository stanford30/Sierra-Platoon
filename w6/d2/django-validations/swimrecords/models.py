from django.db import models
from .validators import *
from django.core import validators as v


class SwimRecord(models.Model):

    # stroke_choices = (
    #     ("front_crawl", "front_crawl"),
    #     ("butterfly", "butterfly"),
    #     ("breast", "breast"),
    #     ("back", "back"),
    #     ("freestyle", "freestyle"),
    # )
    # pass # delete me when you start writing in validations
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    team_name = models.CharField(max_length=100, blank=False)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=100, validators=[valid_stroke])
    distance = models.IntegerField(validators=[v.MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[valid_date])
    record_broken_date = models.DateTimeField(validators=[valid_record_date])
