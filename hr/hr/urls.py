from django.conf.urls import patterns, include, url
from django.conf  import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'users/',include('smartmin.users.urls')),
                       url(r'^',include ('employees.urls')),
                       url(r'^blog/',include('blog.urls')),
                       url(r'^employees/',include('employees.urls')),
                       url(r'^Departments/',include('Departments.urls')),
                       url(r'^leave/',include('leave.urls')),
    # Examples:
    # url(r'^$', 'hr.views.home', name='home'),
    # url(r'^hr/', include('hr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
