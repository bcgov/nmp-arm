#
#  this view inherits from up the chain from
#  two or three others
#  class BaseFormView(FormMixin, ProcessFormView):
#  located in lib/python2.7/site-packages/django/views/generic/edit.py
#  this is where you will find which hooks to override
#  for form validation etc
#
#from django.contrib.auth.decorators import login_required
#from django.core.urlresolvers import  reverse_lazy, Resolver404
#from django.shortcuts import get_object_or_404
#from django.utils.decorators import method_decorator
from django.views.generic.edit import BaseFormView

#
#  sys imports
#
import json
import logging
logger = logging.getLogger( __file__ )

#
#  get this here
#
# https://github.com/thebigspoon/django_1.4_template/blob/master/project/common_utils/mixins/json_response_mixin.py
from common.functions.log_traceback import LogTraceback
from common.mixins.JSONResponseMixin import JSONResponseMixin

# If ``csrf_exempt`` isn't present, stub it.
try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    def csrf_exempt(func):
        return func

class FormApiView( JSONResponseMixin, BaseFormView ):

    http_method_names = [ 'get', 'post', ]
    form_class = None

    error = None

    @csrf_exempt
    def dispatch( self, *args, **kwargs ):
        return super( FormApiView, self ).dispatch( *args, **kwargs )

    def form_invalid( self, form ):
        logger.debug( "Form NOT valid" )
        errors = {}
        for error in list(form.errors.keys()):
            if len( form.errors[ error ] ) == 1:
                errors[ error ] = form.errors[ error ][0]
            else:
                errors[ form.errors[ error ][0] ] = form.errors[ error ][1]
        return self.render_json_object_response( { "result": "error", "errors": errors }, status=400 )

    def form_valid( self, form ):
        logger.debug( "Form IS valid" )

        self.save( form=form )
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        return self.render_json_object_response( { "result": "success", "data": self.object.to_dict() }, **{} )


    def get( self, request, *args, **kwargs ):
        """
            Returns a single JSON object in a JSON list
            representing the model instance
        """
        instance = self.get_object()
        #logger.debug( "get_object() instance = %s" % instance )

        if instance == None:
            if self.error:
                return self.render_json_object_response( { "result": "error",  'error': self.error }, status=404 )
            else:
                return self.render_json_object_response( { "result": "error",  'error': "not found" }, status=404 )

        return self.render_json_object_response( instance, **{} )

    def get_initial( self ):
        initial = self.get_object()
        if initial:
            return initial
        else:
            return {}

    def get_object(self):
        logger.debug( "Getting object...")
        if hasattr( self, 'object' ):
            return self.object.to_dict()

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        raw_json = self.request.body

        #logger.error( "Body: %s" % raw_json )
        parsed = json.loads( raw_json )

        form_values = self.get_initial()

        # only allow 1 level deep of dictionaries and lists
        for key in list(parsed.keys()):
            if type( parsed[key] ) == list or type( parsed[key] ) == dict:
                form_values[ key ] = json.dumps( parsed[key] )
            else:
                form_values[ key ] = parsed[ key ]

        kwargs = {'initial':  form_values.copy() }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': form_values,
                'files': self.request.FILES,
            })
        return kwargs

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        logger.debug( "POST" )
        form_class = self.get_form_class()
        try:
            form = self.get_form( form_class )
            # if the url contains values that are used, pass them in here:
            # form.some_id = self.kwargs['some_id']
        except:
            logger.error( "Error parsing JSON!" )
            LogTraceback()
            return self.render_json_object_response( { 'result': 'error', 'error': 'invalid json' }, status=500 )
        if form.is_valid():
            logger.debug( "VALID" )
            return self.form_valid(form)
        else:
            logger.debug( "inVALID" )
            return self.form_invalid(form)

    def save( self, *args, **kwargs ):
        #logger.debug( "Saving in Mixin..." )
        self.object = kwargs[ 'form' ].save()
