import inspect

class ENUM_TYPE():
    """
    class to sublcass for easier ENUM creation
    assumes that class attributes will have upper() keys and values
    if value is not upper, then you will need to write another
    classmethod that returns keys so you can do easy dot operator
    comparisons

    ----------------------------------------------

    #
    #  now we just define enums with a subclass
    #
    class DEVICE_TYPE( ENUM_TYPE ):
        ANDROID = 'ANDROID'
        IOS = 'IOS'


    #
    #  we can use like this in a model
    #
    type = models.CharField(
                    verbose_name='Type',
                    max_length=30,
                    choices=DEVICE_TYPE.as_enum(),
                    default=DEVICE_TYPE.ANDROID
    )


    #
    #  comparisons:
    #  if we keep class attribute values and keys both uppercase ( as in DEVICE_TYPE example )
    #  and don't write another classmethod to ease comparisons
    #  then they can be done like this
    #
    value_to_compare = 'ANDROID'
    try:
        if getattr( DEVICE_TYPE, value_to_compare ) == value_to_compare:
            # do something grand here
    except AttributeError, ae:
        pass
    """

    @classmethod
    def as_enum( self ):
        dict_values = {}

        for k,v in inspect.getmembers( self ):
            if k.isupper() and not inspect.ismethod( v ) and not inspect.isfunction( v ):
                dict_values[ k ] = getattr( self, k )

        return tuple( dict_values.items() )


    @classmethod
    def get( self, my_value ):
        ''' Used in if statements!!! '''
        
        if not my_value:
            return None
        
        # if the input is really a valid key, then return it!
        if my_value in self.as_dict().keys():
            return my_value
        
        # find the appropriate key for this value!
        for key, value in self.as_enum():
            if value.lower() == my_value.lower():
                return key

        return None

    @classmethod
    def get_value( self, my_value ):
        ''' Used in if statements!!! '''
        
        if not my_value:
            return None
        
        # if the input is really a valid key, then return it!
        if my_value in self.as_dict().keys():
            return self.as_dict()[ my_value ]
        
        # find the appropriate key for this value!
        for key, value in self.as_enum(): #@UnusedVariable
            if value.lower() == my_value.lower():
                return value

        return None

    @classmethod
    def as_dict( self ):
        ''' Used above '''
        dict_values = {}
        
        # Iterate over all items associated with this class
        for e in dir( self ):
            # Skip any that aren't all upper or 'DEFAULT
            if e.isupper() and e != 'DEFAULT':
                # Add to dictionary
                dict_values[ e ] = getattr( self, e )
                
        return dict_values
