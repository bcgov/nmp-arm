#
#  django imports
#
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

#
#  sys imports
#

#
#  app imports
#
from models import Admin

class AdminCreationForm( forms.ModelForm ):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    error_messages = {
            'duplicate_email': _( "A user with that email address already exists." ),
            'password_mismatch': _( "The two password fields didn't match." ),
    }
    password1 = forms.CharField( label=_( "Password" ),
        widget=forms.PasswordInput )

    password2 = forms.CharField( label=_( "Password confirmation" ),
        widget=forms.PasswordInput,
        help_text=_( "Enter the same password as above, for verification." ) )

    class Meta:
        model = Admin
        fields = ( 'email', 'first_name', 'last_name', 'is_active', 'is_superuser' )

    def clean_email( self ):
        # Since Admin.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            Admin._default_manager.get( email=email )  # @UndefinedVariable
        except Admin.DoesNotExist:
            return email
        raise forms.ValidationError( self.error_messages['duplicate_email'] )

    def clean_password2( self ):
        password1 = self.cleaned_data.get( "password1" )
        password2 = self.cleaned_data.get( "password2" )
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'] )
        return password2

    def save( self, commit=True ):
        user = super( AdminCreationForm, self ).save( commit=False )
        user.set_password( self.cleaned_data["password1"] )
        if commit:
            user.save()
        return user


class AdminChangeForm( forms.ModelForm ):
    password = ReadOnlyPasswordHashField( label=_( "Password" ),
        help_text=_( "Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>." ) )

    class Meta:
        model =Admin
        #fields = [ 'email', 'first_name', 'last_name', 'is_active', 'is_superuser' ]

    def __init__( self, *args, **kwargs ):
        super( AdminChangeForm, self ).__init__( *args, **kwargs )
        f = self.fields.get( 'user_permissions', None )
        if f is not None:
            f.queryset = f.queryset.select_related( 'content_type' )

    def clean_password( self ):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
