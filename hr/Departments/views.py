from .models import*
from smartmin.views import *

class departmentsCRUDL(SmartCRUDL):
    model=departments
    actions=('create','list')
    permissions=True

    class List(SmartListView):
        field = ('name')

    class Create(SmartCreateView):    
        field = ('name')

    #class Update(SmartUpdateView):    
        #field = ('name')
