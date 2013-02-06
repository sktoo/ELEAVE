from django.db import models
from smartmin.models import SmartModel

class departments(SmartModel):
    name=models.CharField(max_length=128,help_text="Department Name")
    def __unicode__(self):
        return self.name
