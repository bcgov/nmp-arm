import os 

def valid_password( password ):
    if password in open( os.path.dirname( os.path.abspath( __file__ ) ) + '/disallowed_passwords.txt' ).read():
        return False

    return True
