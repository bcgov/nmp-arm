#
#  django improts
#
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

#
#  sys imports
#

#
#  app imports
from models import Admin

from forms import AdminChangeForm
from forms import AdminCreationForm

class MyAdminAdmin(UserAdmin):
    # The forms to add and change user instances
    form = AdminChangeForm
    add_form = AdminCreationForm

    # The fields to be used in displaying the Admin model.
    # These override the definitions on the base AdminAdmin
    # that reference specific fields on auth.Admin.
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'last_login' )
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',  )}),
        (_('Personal info'), {'fields': ( 'first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ( 'is_active', 'is_superuser', 'groups' )}),
        #(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_superuser' )}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name' )
    ordering = ('email',)
    filter_horizontal = ('groups',)

# Now register the new AdminAdmin...
admin.site.register( Admin, MyAdminAdmin )
# ... and, since we're not using Django's builtin permissions,
# unregister the Group model from admin.
admin.site.unregister( Group )
