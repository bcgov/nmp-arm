import logging
import os
logger = logging.getLogger( __file__ )

# create_dirs
def create_dirs( root_path, dir_list ):

    if type( root_path ) != str:
        raise Exception( "'root_path' not a string!")

    if type( dir_list ) != list:
        raise Exception( "'dir_list' not a list!" )

    # set base path
    path = root_path

    # reverse order
    dir_list.reverse()

    # loop over each dir
    while dir_list:
        dir_item = str( dir_list.pop() )
        path = os.path.join( path, dir_item )

        if not os.path.exists( path ):
            os.mkdir( path )

    return path.replace( root_path, '' )

