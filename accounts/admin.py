from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from models import HereUser
from forms import UserChangeForm, UserCreationForm

class HereUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'nickname', 'realname', 
        'gender', 'mobile', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields':('nickname','realname',
            'gender', 'mobile', 'birthday', 'mydesc')}),
        ('Permissions', {'fields': ('is_admin', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username','email',)
    ordering = ('-id',)
    filter_horizontal = ()

admin.site.register(HereUser, HereUserAdmin)

admin.site.unregister(Group)
