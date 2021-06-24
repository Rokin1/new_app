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
    level = models.IntegerField(verbose_name='Class Level', default=1)
    notes = models.TextField()
    class Meta:
        verbose_name_plural = 'Waitlist entries'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        