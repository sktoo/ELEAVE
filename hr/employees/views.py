from .models import *
from smartmin .views import *
from django.conf import settings
from django.contrib.auth.models import User,Group
from leave.models import*
import random
import string
from django import forms
from datetime import datetime,timedelta
from django.core.mail import send_mail,mail_admins

class EmployeesForm(forms.ModelForm):

    def clean_dateJoined(self):
        dateJoined = self.cleaned_data['dateJoined']
        #import pdb; pdb.set_trace()
        today=datetime.now().date()
        if dateJoined > today:
            raise forms.ValidationError("Date joined must not be in the future")
        return dateJoined

    class Meta:
        model = employees

class employeesCRUDL(SmartCRUDL):
    model= employees
    actions=('create','update','list')
    permissions=True

    class List(SmartListView):
        fields=('lastName','firstName','gender','email','cv','dateJoined','department')
    class Create(SmartCreateView):    
        fields=('lastName','firstName','gender','email','cv','dateJoined','department')
        form_class = EmployeesForm
        
        #import pdb; pdb.set_trace()
        def pre_save(self,obj):
            obj= super(employeesCRUDL.Create,self).pre_save(obj)
            obj.token= ''.join(random.choice(string.ascii_uppercase + string.digits)for x in range(32))
            user=User.objects.create(username=obj.email,email=obj.email,password=obj.firstName)
            user.email_user("HR application Account activation","Ur account has been created just go to this link \n\n http://localhost:employees/activate/%s \n\n after activated ur account login using ur email adress as username  and password dont respond it  \n\n ."%obj.token,"habm")

            group = Group.objects.get(name ='Editor')
            user.groups.add(group)
            user.first_name=obj.firstName
            user.last_name=obj.lastName
            user.email= obj.email
            #user.set_unusable_password()
            mail_admins("Important  notification"," A new  employee has been added into your Company")
            mail_admins("Important  notification"," A new  employee has been added into your Company : %s %s " %(obj.firstName,obj.lastName))
            #send_mail(" leave notification","you leave apiilication has been sent : %s %s %s" %(obj.firstName,obj.lastName,obj.email),'habirobert@gmail.com',['obj.email'])
            user.email_user("ur leave application has been received","Do not  respond ")
            user.save()

            obj.user=user
            #obj.is_active= False
            obj.save()
            return obj
        #def save(self,*args,**kwargs):
            #if self.dateJoined<datetime.now():
               #super (self).save(*args,**kwargs)
        #def save(self,*args,**kwargs):
            #if self.lastName!="robert":
                #super(employees,self).save(*args,**kwargs)
                
                
                
            

    class Update(SmartUpdateView):
        fields=('lastName','firstName','gender','email')
