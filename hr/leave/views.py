from .models import *
from smartmin.views import *
from django import forms
from django.contrib.auth.models import User,Group

class LeaveForm(forms.ModelForm):
	
	def clean(self):
		cleaned_data=super(LeaveForm,self).clean()
		dateLeave=self.cleaned_data['dateLeave']
		dateReturn=self.cleaned_data['dateReturn']

		if dateReturn < dateLeave:
			raise forms.ValidationError("dateReturn  must be greater than dateLeave")
		return cleaned_data

	class Meta:
		model=leave

   
class leaveCRUDL(SmartCRUDL):
    model=leave
    actions = ('create','update','list')
    permissions =True

    class List(SmartListView):
        fields =('requestor','typeLeave','dateLeave','dateReturn','status','comment')

	def derive_queryset(self,**kwargs):
		queryset=super(leaveCRUDL.List,self).derive_queryset(**kwargs)
		return queryset.filter(requestor=self.request.user)#to work on 2morro

    class Create(SmartCreateView):
        fields= ('typeLeave','dateLeave','dateReturn','comment')
	form_class = LeaveForm

	def pre_save(self,obj):
		obj= super (leaveCRUDL.Create,self).pre_save(obj)
		obj.requestor=self.request.user
		return obj
		


    class Update(SmartUpdateView):
        fields= ('requestor','typeLeave','dateLeave','dateReturn','status','comment')
	form_class= LeaveForm
