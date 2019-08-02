import logging
logger = logging.getLogger(__file__)

from conduit.subscribe import subscribe, avoid, match
from example.models import Bar, Baz, Foo

#
#  create a resource conduit
#  as just module-level functions
#
def build_pub(self, request, *args, **kwargs):
    pub = []
    pub.append(request.method.lower())
    if kwargs.get(self.Meta.pk_field, None):
        pub.append('detail')
    else:
        pub.append('list')
    kwargs['pub'] = pub 
    return (request, args, kwargs)

@subscribe(sub=[
    'get',
    'post',
    'put',
    'delete',
    'head',
    'options',
    'trace'
])  
def return_response(self, request, *args, **kwargs):
    response_data = { 
        'success' : True ,
        'status' : '200' , 
    }   
    return response_data


#
#  create a resource conduit
#  as class methods
#
class ConduitBaseMixin(object):

    def build_pub(self, request, *args, **kwargs):
        """ 
        Builds a list of keywords relevant to this request
        """
        pub = []
        pub.append(request.method.lower())
        if kwargs.get(self.Meta.pk_field, None):
            pub.append('detail')
        else:
            pub.append('list')
        kwargs['pub'] = pub 
        return (request, args, kwargs)

    @subscribe(sub=[
        'get',
        'post',
        'put',
        'delete',
        'head',
        'options',
        'trace'
    ])  
    def return_response(self, request, *args, **kwargs):
        response_data = { 
            'success' : True ,
            'status' : '200' , 
        }   
        return response_data

#
#  create a resource conduit as class methods.
#  add internal *private* class methods
#  that the conduit methods
#  will call into during execution.
#  using the dynamic rebinding method approach
#  (https://github.com/akoumjian/django-conduit/commit/44a29f61979430a45cd07423cc71eb254f0b4673)
#  this will fail because self ( and subsequent mro lookups )
#  only reference the Conduit subclass tree
#  and not necessarily the parent class of the method we are calling.
#  Using the dynamic __bases__ approach 
#  solves this issue and allows people to write
#  *private* class mixins in an intuitive format
#
class ConduitMixinPrivateer(object):

    def _i_am_private( self ):
        x = 2 + 2
        return True

    def build_pub(self, request, *args, **kwargs):
        """ 
        Builds a list of keywords relevant to this request
        """
        pub = []
        pub.append(request.method.lower())
        if kwargs.get(self.Meta.pk_field, None):
            pub.append('detail')
        else:
            pub.append('list')
        kwargs['pub'] = pub 
        self._i_am_private()
        return (request, args, kwargs)

    @subscribe(sub=[
        'get',
        'post',
        'put',
        'delete',
        'head',
        'options',
        'trace'
    ])  
    def return_response(self, request, *args, **kwargs):
        response_data = { 
            'success' : True ,
            'status' : '200' , 
        }   
        self._i_am_private()
        return response_data
