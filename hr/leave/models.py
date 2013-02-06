from django.db import models
from smartmin.models import  SmartModel
from employees.models import *
from django.contrib.auth.models import User


class leave(SmartModel):
    typesleave=(
        ('ann',"annual"),
        ('oth',"other"),

)

    stat=(
        ('pending',"pending"),
        ('approved',"approved"),
        ('canceled',"canceled")
)

    #requestor=models.ForeignKey(employees,help_text="employee who is requesting a leave")
    requestor=models.ForeignKey(User,help_text="employee who is requesting a leave")
    typeLeave=models.CharField(help_text="specify the leave type", choices=typesleave,max_length=3)
    dateLeave= models.DateField(help_text="Date to leave")
    dateReturn =models.DateField(help_text="Date to return")
    status=models.CharField(max_length=8,choices=stat,help_text="status of the leave" , default='pending')
    comment= models.TextField(max_length="200", help_text="Any comment if not approved")

    def __unicode__(self):
        return "%s_%s" %(self.requestor,self.typeLeave)

