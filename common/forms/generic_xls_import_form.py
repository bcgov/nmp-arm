#
#  django imports
#
from django import forms
from django.conf import settings
from django.forms.util import ValidationError
from django.utils.translation import ugettext_lazy as _

#
#  system imports
#
from os import path
from datetime import datetime
import logging
import zipfile
logger = logging.getLogger( __file__ )

#
#  common imports
#
from common.functions.filesystem import create_dirs


class GenericXLSImportForm( forms.Form ):

    datafile  = forms.FileField( label=_('Upload an Excel Spreadsheet') )
    
    named_file = '%s_import'

    def clean_datafile(self):
        '''
        Clean datafile
        '''
        f = self.cleaned_data['datafile']
        valid_file, error = self.validate(f)
        if not valid_file:
            raise ValidationError("A problem occurred: %s" % error)

    def zip_check( self, ext, zip_file ):
        '''
        Check to see if file is zip'ed
        '''
        if not True in [ info.filename.endswith('xls') for info in zip_file.infolist() ]:
            return False
        return True
    
    def validate( self, uploaded_file ):
        '''
        Validate uploaded file
        '''

        now = datetime.now()

        # ---- Resave file to a temporary filename
        tmp_dir = create_dirs( settings.UPLOAD_DIR, [ now.year, now.month, now.day ] )
        local_filename = path.join( tmp_dir, self.named_file % ( now.strftime( "%H.%M" ) ) )

        logger.info( "Resaving [%s] to [%s]" % ( uploaded_file.name, local_filename ) )
        destination = open(local_filename, 'wb+')
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
        destination.close()

        if zipfile.is_zipfile( local_filename ):
            # Handle zip archives
            logger.info( "File [%s] is not a valid Zip Archive" % uploaded_file.name )

            # ---- Unzip temporary file
            logger.info( "Unzip'ng file [%s]" % local_filename )
            zfile = zipfile.ZipFile( local_filename )
    
            # ---- Check contents of zip file
            if not self.zip_check('xls', zfile):
                logger.error( "Found Zip Archive but no file with a .xls extension found inside.")
                return False, 'Found Zip Archive but no file with a .xls extension found inside.'

            # Loop over each file in the archive
            for info in zfile.infolist():
    
                if info.filename.startswith( '__MACOSX' ):
                    continue
                
                data = zfile.read( info.filename )
                real_filename = path.join( tmp_dir, info.filename )
    
                logger.info( "Reading file [%s] from Zip archive and saving to [%s]" % ( info.filename, real_filename ) )
    
                try:
                    fout = open( real_filename, "wb" )
                except:
                    logger.error( "Unable to open [%s] for writing" % real_filename )
                    raise Exception( 'unable to open %s' % real_filename )
    
                fout.write(data)
                fout.close()
                
        else:
            # Handle raw files
            real_filename = local_filename

        self.raw_file = real_filename
        self.raw_name = local_filename
        return True, None