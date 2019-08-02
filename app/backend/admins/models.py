#
# django imports
#
from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, PermissionsMixin, BaseUserManager )
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

#
# sys imports
#


class AdminManager( BaseUserManager ):

    def create_user( self, email, password=None, **extra_fields ):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError( 'The given email address must be set' )
        email = AdminManager.normalize_email( email )
        user = self.model( email=email,
                           is_active=True,
                           is_superuser=False,
                           last_login=now,
                           date_joined=now,
                           **extra_fields )

        user.set_password( password )
        user.save( using=self._db )
        return user

    def create_superuser( self, email, password, **extra_fields ):
        u = self.create_user( email, password, **extra_fields )
        u.is_active = True
        u.is_staff=True
        u.is_superuser = True
        u.save( using=self._db )
        return u

class Admin( AbstractBaseUser, PermissionsMixin ):
    """
    An abstract base class implementing a fully featured Admin model with
    admin-compliant permissions.

    Email, password and email are required. Other fields are optional.
    """
    first_name = models.CharField( _('first name' ), max_length=30, blank=True )
    last_name = models.CharField( _('last name' ), max_length=30, blank=True )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )

    is_active = models.BooleanField( _('active' ), default=True,
                                     help_text=_( 'Designates whether this user should be treated as '
                                                  'active. Unselect this instead of deleting accounts.' ) )

    date_joined = models.DateTimeField( _('date joined' ), default=timezone.now )

    is_staff = True

    objects = AdminManager( )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name',]

    class Meta:
        app_label = 'admins'
        #db_connection = 'default'
        db_table = 'django_admins'
        verbose_name = _( 'Admin' )
        verbose_name_plural = _( 'Admins' )

    def __unicode__( self ):
        return self.email

    def get_absolute_url( self ):
        return "/admin/%s/" % urlquote( self.username )

    def get_full_name( self ):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % ( self.first_name, self.last_name )
        return full_name.strip( )

    def get_short_name( self ):
        "Returns the short name for the user."
        return self.first_name

    def email_user( self, subject, message, from_email=None ):
        """
        Sends an email to this Admin
        """
        send_mail( subject, message, from_email, [self.email] )

