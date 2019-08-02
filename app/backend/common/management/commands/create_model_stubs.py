
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
import os,sys,string
import logging
logger=logging.getLogger(__file__)


def create_or_replace_app_subdirs( app_path, dir_name ):
    dir_path = os.path.join( app_path, dir_name )
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
    
def import_mods( mods_string, class_string ):
    split_mods = string.split( mods_string, '.' )
    split_mods.reverse()
    logger.debug( "[ IMPORT ] %s" % mods_string )
    form_module = __import__( '%s' % mods_string )
    split_mods.pop() # get rid of first mod since we are already there
    mod = form_module
    while split_mods:
        mod = getattr( mod, split_mods.pop() )
    # get class from last mod
    class_object = getattr( mod, class_string )
    return class_object

def get_model_by_content_type( model_name ):
    '''
    return a dictionary with
    model_name and model_app_label
    '''
    logger.debug( "[ GETTING ] model_name = %s" % model_name )
    content_type_model = ContentType.objects.filter( model__iexact=model_name)
    if content_type_model.exists() and content_type_model.count() == 1:
            content_model_name = content_type_model[0].model
            app_label = content_type_model[0].app_label
            full_app_label = None
                

            #
            #  the content_type.model_name is different than model.model_name
            #  so we need content_type.model_name to get model class
            #  and then we override it with model.object_name
            #
            model = get_model( app_label, content_model_name )
            object_model_name = model._meta.object_name
            full_app_label = get_app( 'admin_users' ).__name__

    
            return { 'model_name' : object_model_name, 'model_name_app_label' : full_app_label }
    else:
            raise CommandError( "You were looking for model class [%s], it was not found. Did you spell it right? Does it exist in <app_name>/<forms_dir>/<form>.py structure?" % model_name )
            sys.exit( 1 )

class Command(BaseCommand):
    args = ''
    help = '' + \
           ''
    option_list = BaseCommand.option_list + (

                                                make_option('-m','--model-name',
                                                         type='string',
                                                         dest='model_name',
                                                         default=False,
                                                         help='the model name that we will create stubs for [ ASSUMPTION ]: the \
                                                         the models are held in a directory called models'),  

                                                make_option('-t','--stub-type',
                                                         type='string',
                                                         dest='stub_type',
                                                         default=False,
                                                         help='the stub type we want to create -- either "admin" or "forms" or "api" '),  
                                             
                                                make_option('-f','--model-form-name',
                                                         type='string',
                                                         dest='model_form_name',
                                                         default=False,
                                                         help='the model form that will be used to validate, clean data for --model-name [ ASSUMPTION ]: the \
                                                            --model-name that contains the models also has a directory called forms/'),
                                            
                                                make_option('-d','--dry-run',
                                                         action='store_false',
                                                         dest='dry_run',
                                                         default=False,
                                                         help='do not write out the classes to DIRS...just print'),

                                            
                                             
                                            )
    def handle(self, *args, **options):
        BASE_TEMPLATE_PATH = os.path.join( settings.ABSOLUTE_PATH, 'templates/autocreate_templates/model_%s.template' )
        kwargs={}  # @UnusedVariable
        include_fields = []  # for creating *both* model admins and forms
        exclude_fields = []  # for creating *both* model admins and forms
        inline_admins = []  # only for creatin model admins
        fkey_models = [] # for api only
        model_form = {} # for api only

        #
        #  qc
        #
        if not options['model_name'] and not options['stub_type']:
            raise CommandError('You need to provide  a --model-name and --stub-type [ forms, admin, api ]')
        if options['stub_type'] not in [ 'forms', 'admin', 'api' ]:
            raise CommandError('--stub-type flag must be set to "forms" or "admin" or "apis" ')
        if options['stub_type'] == 'api' and not options['model_form_name']:
            raise CommandError('where --stub-type is "api" you must be set --model-form-name flag')          

        #
        #  main
        #
        content_type_model = ContentType.objects.filter( model__iexact=options['model_name'] )
        logger.debug("[ TEMPLATE ]: %s" % BASE_TEMPLATE_PATH)
        BASE_TEMPLATE_PATH = BASE_TEMPLATE_PATH % options['stub_type']
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
            #  and looking the __name__ to understand 
            #  where it's imported from
            #  where is something like <module>.app_name.models
            #
            full_app_label = get_app(app_label).__name__
        
            #
            #
            #  __path__ used to get full path for writes...gives back full path
            #  to an apps's model directory
            #
            #
            relative_app_path = get_app(app_label).__path__[0]   
            1
            #
            #
            #  try to import model form or
            #  throw error
            #
            #
            if options['stub_type'] == 'api':
                try:
                    full_forms_import = string.replace( full_app_label, 'models', 'forms' )
                    model_form_class = import_mods( full_forms_import, options['model_form_name'])
                    model_form.update( { 'model_form' : model_form_class.__name__, 'model_form_app_label': full_forms_import } )
                    logger.debug( "[ FORM ]: success retrieved model form = %s" % model_form )
                except Exception, e:
                    logger.exception( e )
                    raise CommandError( "it seems the model-form class you passed in was not found. Did you spell it right? Does it exist in <app_name>/<forms_dir>/<form>.py structure?")
                    sys.exit( 1 )
        

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
                            exclude_fields.append( [ name,  string.strip( field._description().split(':')[1] ) ] )
                            if options['stub_type'] == 'api':
                                #
                                #  skip over fkey of auth user for now
                                #
                                if name != 'user':
                                    #
                                    # 
                                    #  FIGURE OUT HOW WE GET TO FKEY FIELD MODEL NAME
                                    #
                                    #
                                    template_object = get_model_by_content_type( field.model.__name__ )
                                    # update the object name to be api import
                                    model_label = template_object['model_name_app_label']
                                    api_label = string.replace(model_label, 'models', 'api' )
                                    template_object.update( { 'model_name_app_label' : api_label } )
                                    template_object.update( { 'field_name' : name } )
                                    fkey_models.append( template_object )
                        else: #o2o or fkey
                            #logger.debug( "o2o  or fkey FROM this model")
                            if not hasattr( field, 'parent_model'):  # skips fkeys that are <model>_set()
                                exclude_fields.append( [ name,  string.strip( field._description().split(':')[1] ) ] )
                                if options['stub_type'] == 'api':
                                    #
                                    #  skip over fkey of auth user for now
                                    #
                                    if name != 'user':
                                        #
                                        # 
                                        #  FIGURE OUT HOW WE GET TO FKEY FIELD MODEL NAME
                                        #
                                        #
                                        template_object = get_model_by_content_type( field.model.__name__ )
                                        # update the object name to be api import
                                        model_label = template_object['model_name_app_label']
                                        api_label = string.replace(model_label, 'models', 'api' )
                                        template_object.update( { 'model_name_app_label' : api_label } )
                                        template_object.update( { 'field_name' : name } )
                                        fkey_models.append( template_object )
                    else: # standard field#
                        #logger.debug( "standard field")
                        if name != 'id':  # we want all standard fields except ID
                            include_fields.append( [ name,  string.strip( field._description().split(':')[1] ) ] )
                        
   
            #
            #
            #  render templates
            #
            #
            mod_context = {
                    'app_label' : full_app_label,
                    'model_name' : model_name,
                    'module_name' : module_name,
                    'include_fields' : include_fields,
                    'exclude_fields'  : [] # we want excluded fields in our model forms by default ,
            }
            if options['stub_type'] == 'admin':
                mod_context = {
                    'inline_admins' : inline_admins,
                    'show_fields' : include_fields + exclude_fields,
                    'search_fields' : [ i for i in include_fields if i not in exclude_fields ] ,
                    'order_fields' : [ include_fields[0] ],
                    'filter_fields' : [ i for i in include_fields if i not in exclude_fields ],
                    'app_label' : full_app_label,
                    'model_name' : model_name,
                    'module_name' : module_name,
                    'include_fields' : include_fields,
                    'exclude_fields'  : exclude_fields,
                }
            elif options['stub_type'] == 'api':
                mod_context = {

                    'app_label' : full_app_label,
                    'fkey_models' : fkey_models, 
                    'model_form' : model_form,
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
            create_or_replace_app_subdirs( os.path.dirname( relative_app_path  ), options['stub_type'] )
            #
            #
            #  write out the model_class
            #
            #    
            import_type = 'Admin'
            if options['stub_type'] == 'api': 
                import_type = 'Resource'
            elif options['stub_type'] == 'forms': 
                import_type = 'Form'
                
            
    
            if not options['dry_run']:
                write_model_form( 
                    os.path.join( 
                        os.path.dirname( relative_app_path ), options['stub_type'], "%s_model_%s.py" % ( ctype_model_name, import_type.lower() if import_type != 'Resource' else 'api' )
                    ), 
                    model_form_class )
            else:
                logger.debug('\n\n\n')            
                logger.debug('---------------------------------------------------')
                logger.debug('------- COPY THESE TO YOUR MODEL FORMS ------')
                logger.debug('---------------------------------------------------\n')
                logger.info( model_form_class )
            

            if not options['dry_run']:
                write_to_init( 
                    os.path.join( 
                        os.path.dirname( relative_app_path ), options['stub_type'], "__init__.py"
                    ), 
                    "from %s_model_%s import %sModel%s\n" % 
                    ( module_name, import_type.lower() if import_type != 'Resource' else 'api', model_name, import_type )  )
            else:
                logger.debug('\n\n\n')
                logger.debug('---------------------------------------------------')
                logger.debug('------- __INIT__.py ------')
                logger.debug('---------------------------------------------------\n')
                logger.info( "from %s_model_%s import %sModel%s\n" % 
                    ( module_name, import_type.lower() if import_type != 'Resource' else 'api', model_name, import_type )   )
                logger.debug('\n\n\n')
            
            
        else:
            raise CommandError('That model name does not exist yet in content_types table. Have you added it to settings.INSTALLED_APPS and ran syncdb?')
