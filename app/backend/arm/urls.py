#
#  django imports
#
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models() 
admin.autodiscover()
from django.contrib.messages import get_messages
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.views.generic import RedirectView
from django.views.generic import TemplateView

#
#  system imports
#
from os import path

#
#  app imports
#
#handler404 = 'PracticeGround.mobile.views.Custom404Handler'
#handler500 = 'PracticeGround.mobile.views.Custom500Handler'

from arm.views.WorksheetView import WorksheetView

def static(request, template_name):

    if 'employee_id' in request.session.keys():
        employee = Employee.objects.get( id = request.session['employee_id'] )
    else:
        employee = None

    c = {
        'page_name': 'Static Page',
        'site': Site.objects.get_current(),
        'version': settings.SERVERVERSION,
        'messages' : get_messages( request ),
        'employee' : employee
    }

    # render page
    return render_to_response( template_name, c, )


urlpatterns = patterns('',
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/css' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/font'% path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^img/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/img' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/js' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),

    url( r'/^$', WorksheetView.as_view(), name='worksheet'  ),
    url( r'^$', WorksheetView.as_view(), name='worksheet'  ),
    url( r'^thankyou/$', TemplateView.as_view( template_name="thankyou.html" ), name="thankyou" ),
    #url( r'/^$', TemplateView.as_view( template_name="bc_worksheet.html" ) ),
    #url( r'^worksheet/$', TemplateView.as_view( template_name="bc_worksheet.html" ) ),
    url( r'^admin/', include(admin.site.urls) ),
    #url( r'^employee/', include( 'inout_board.employees.urls', app_name='employees', namespace='employees' ) ),
    #url( r'^district/', include( 'inout_board.districts.urls', app_name='districts', namespace='districts' ) ),

    #
    #  Examples
    #
    #url( r'^client/',       include( 'PracticeGround.clients.urls',    app_name='clients',    namespace='client'    ) ),
    #url( r'^api/v1/therapist/', include( 'PracticeGround.therapists.urls_api', app_name='therapists', namespace='therapist_api' ) ),
    #url( r'^api/v1/client/', include( 'PracticeGround.clients.urls_api', app_name='clients', namespace='client_api' ) ),
    #url( r'', include( 'PracticeGround.api.urls' ) ),
    #url( r'', include( 'Industry.urls' ) )
)
