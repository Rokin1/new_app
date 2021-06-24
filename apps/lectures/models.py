from django.db import models
from apps.utils.models import Timestamps
# Create your models here.
class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField()
    slides_url = models.CharField(max_length=250)
    