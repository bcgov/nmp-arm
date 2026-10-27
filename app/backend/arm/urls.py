#
#  django imports
#
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path
#
#  system imports
#

#
#  app imports
#
#handler404 = 'PracticeGround.mobile.views.Custom404Handler'
#handler500 = 'PracticeGround.mobile.views.Custom500Handler'

from arm.views.WorksheetView import WorksheetView
from arm.views.PdfView import PdfView

urlpatterns = [

    re_path(r'^arm/$', WorksheetView.as_view(), name='main' ),
    re_path( r'^$', WorksheetView.as_view(), name='worksheet'  ),
    re_path( r'^thankyou/$', TemplateView.as_view( template_name="thankyou.html" ), name="thankyou" ),
    re_path( r'^pdf/$', PdfView.as_view(), name='pdf'),
    path('admin/', admin.site.urls),
]