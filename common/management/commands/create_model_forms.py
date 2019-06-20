
#
#  django imports
#
from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model
from django.db.models import get_app
from django.contrib.contenttypes.models import ContentType
from django.template import Context, Template
from django.conf import settings

#
#  sys imports
#
from optparse import make_option
import os,string
import logging
logger=logging.getLogger( __file__ )

BASE_TEMPLATE_PATH = os.path.join( settings.ABSOLUTE_PATH, 'templates/autocreate_templates/model_form.template' )

def create_or_replace_app_subdirs( app_path, dir_name ):
    dir_path = os.path.join( app_path, dir_name )
    # init_path = os.path.join( app_path, dir_name, '__init__.py' )
    if not os.path.exists( dir_path ):
        os.mkdir( dir_path )

def write_model_form( file_path, rendered_class ):
    logger.debug( "[ WRITING ]: %s" % file_path )
    writer = open( file_path, "w" )
    writer.write( rendered_class )
    writer.close()

def write_to_init( file_path, rendered_class ):
    logger.debug( "[ WRITING ]: %s" % file_path )
    write_mode = "a"
    if not os.path.exists( file_path ):
        write_mode = "w"
    writer = open( file_path, write_mode )
    writer.write( rendered_class )
    writer.close()  

class Command(BaseCommand):
    args = ''
    help = '' + \
           ''
    option_list = BaseCommand.option_list + (

                                                make_option('-m','--model-name',
                                                         type='string',
                                                         dest='model_name',
                                                         default=False,
                                                         help='the model name that we will be trying to create a JSON API for. [ ASSUMPTION ]: the \
                                                         the models are held in a directory called models'),  
                                             
                                            )
    def handle(self, *args, **options):
        kwargs={}  # @UnusedVariable
        include_fields = []
        exclude_fields = []

        #
        #  qc
        #
        if not options['model_name']:
            raise CommandError('You need to provide  a --model-name and --model-form-name')

        #
        #  main
        #
        content_type_model = ContentType.objects.filter( model__iexact=options['model_name'] )
        if content_type_model.exists() and content_type_model.count() == 1:
            model_name = content_type_model[0].model
            app_label = content_type_model[0].app_label

            #
            #  the content_type.model_name is different than model.model_name
            #  so we need content_type.model_name to get model class
            #  and then we override it with model.object_name
            #
            model = get_model( app_label, model_name )
            module_name = model._meta.module_name
            ctype_model_name = model_name # save the content_type version for later use
            model_name = model._meta.object_name
            
            
            #
            #
            #  get the app name
            #  in weird nested situations 
            #  where apps are inside other apps
            #  we don't know full context path
            #  we we finagle it by getting app
            #  and looking the name to understand 
            #  where it's imported from
            #  where is something like <module>.app_name.models
            #
            full_app_label = get_app(app_label).__name__

            opts = getattr( model, '_meta', None )
            if not opts:
                raise CommandError('Cannot find _meta attribute on model')

            for f in opts.get_all_field_names():
                field, model, direct, m2m = opts.get_field_by_name(f)  # @UnusedVariable
                name = field.name
                logger.info( "[ FIELD ]: %s " % name )
                if not direct: # relation or many field from another model
                    name = field.get_accessor_name()
                    field = field.field
                    if field.rel.multiple: # m2m or fk to this model
                        #logger.debug( "m2m or fkey TO this model")
                        #exclude_fields.append( name )
                        pass
                    else: # o2o
                        #logger.debug( "o2o TO this model")
                        #exclude_fields.append( name )
                        pass
                else: # relation, many or field from this model
                    if field.rel: # relation or many field
                        if hasattr(field.rel, 'through'): # m2m
                            #logger.debug( "m2m FROM this model")
                            exclude_fields.append( name )
                        else: #o2o or fkey
                            #logger.debug( "o2o  or fkey FROM this model")
                            if not hasattr( field, 'parent_model'):  # skips fkeys that are <model>_set()
                                exclude_fields.append( name )
                    else: # standard field#
                        #logger.debug( "standard field")
                        if name != 'id':
                            include_fields.append( [ name,  string.strip( field._description().split(':')[1] ) ] )
                        

            
            
            #
            #
            #  render templates
            #
            #
            logger.info( include_fields )
            mod_context = {
                    'app_label' : full_app_label,
                    'model_name' : model_name,
                    'module_name' : module_name,
                    'include_fields' : include_fields,
                    'exclude_fields'  : exclude_fields,
            }
            context  = Context( mod_context )
            t = Template( open( BASE_TEMPLATE_PATH, "r" ).read() )
            model_form_class = t.render( context )

            #
            #
            #  check for existence of app subdirs
            #
            #
            create_or_replace_app_subdirs( os.path.dirname( get_app(app_label).__path__[0]  ), 'form' )
            #
            #
            #  write out the model_class
            #
            #
            write_model_form( 
                os.path.join( 
                    os.path.dirname( get_app(app_label).__path__[0] ), 'form', "%s_model_form.py" % ctype_model_name 
                ), 
                model_form_class )
            
            logger.debug('\n\n\n')
            logger.debug('---------------------------------------------------')
            logger.debug('------- COPY THESE TO YOUR MODEL FORMS ------')
            logger.debug('---------------------------------------------------\n')
            logger.info( model_form_class )
            
            logger.debug('\n\n\n')
            logger.debug('---------------------------------------------------')
            logger.debug('------- __INIT__.py ------')
            logger.debug('---------------------------------------------------\n')
            
            write_to_init( 
                os.path.join( 
                    os.path.dirname( get_app(app_label).__path__[0] ), "form", "__init__.py"
                ), 
                "from %s_model_form import %sModelForm\n" % ( module_name, model_name )  )
            logger.info("from %s_model_form import %sModelForm" % ( module_name, model_name )  )
            logger.debug('\n\n\n')
            
            
        else:
            raise CommandError('That model name does not exist yet in content_types table. Have you added it to settings.INSTALLED_APPS and ran syncdb?')
