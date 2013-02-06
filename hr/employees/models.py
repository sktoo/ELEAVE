from django.db import models
from smartmin.models import SmartModel
from Departments.models import *
from django.contrib.auth.models import User
#from models.db import models


#class Departments (SmartModel):
    #departmentName=models.CharField(max_length=128,help_text="department Name")

    #def __unicode__(self):

        #return self.departmentName


class employees(SmartModel):
    gender=(
        ('M',"Male"),
        ('F',"Female")
        )
    lastName=models.CharField(max_length=128,
                              help_text="last name ")
    firstName=models.CharField(max_length=128,
                               help_text="first name ")

    
    email=models.EmailField(help_text="your email")

    cv=models.FileField(upload_to="cv",help_text="the employee cv")
    
    gender=models.CharField(help_text="gender of the employee",choices=gender,max_length=1)

    dateJoined=models.DateField(help_text="date he/she joined the institution")

    department=models.ForeignKey(departments,help_text="department")
    
    user=models.ForeignKey(User,help_text="the user account associated wit this employee")

    
    
    def __unicode__(self):
        return self.lastName

  
    
