from django.db.models import get_models
from django.db.models.query import QuerySet
from pprint import PrettyPrinter

def dprint(my_object, stream=None, indent=1, width=80, depth=None):
    """
    A small addition to pprint that converts any Django model objects to dictionaries so they print prettier.

    h3. Example usage

    >>> from toolbox.dprint import dprint
    >>> from app.models import Dummy
    >>> dprint(Dummy.objects.all().latest())
        {'first_name': u'Ben',
         'last_name': u'Welsh',
         'city': u'Los Angeles',
         'slug': u'ben-welsh',
    """
    # Catch any singleton Django model object that might get passed in
    if is_model( my_object ):
            # Convert it to a dictionary
            my_object = my_object.__dict__

    # Catch any Django QuerySets that might get passed in
    elif isinstance(my_object, QuerySet):
        # Convert it to a list of dictionaries
        my_object = [i.__dict__ for i in my_object]

    # Pass everything through pprint in the typical way
    printer = PrettyPrinter(stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(my_object)

def is_model( my_object ):
    for m in get_models():
        if isinstance( my_object, m ):
            return True

    return False
