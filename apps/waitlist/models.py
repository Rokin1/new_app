from django.db import models
from apps.utils.models import Timestamps
# Create your models here.
class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(
        verbose_name='email address',
        max_length=200,
        unique=True,
    )
    notes = models.TextField()
    class Meta:
        verbose_name_plural = 'Waitlist entries'
        