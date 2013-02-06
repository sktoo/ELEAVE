# Create your views here.
from smartmin.views import *
from .models import *

class PostCRUDL(SmartCRUDL):
    model=Post
    actions= ('create','update','list')
    permissions=True


    class Update(SmartUpdateView):
        fields=('title','body')

    
    def get_body(self,obj):
        """show only  first 10 words for long bodies"""
        if (len.obj)< 100 :
            return obj.body
        else :
            return "".join(obj.body.split(" ")[0:10])+".."

        
           
    
    class List(SmartListView):
        search_fields=('title__icontains','body__icontains')
        default_order='title'

       


        
