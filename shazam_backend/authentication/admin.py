from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Status


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class StatusInline(admin.StackedInline):
    model = Status
    can_delete = False
    verbose_name_plural = 'Status'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, StatusInline)
    list_display = ('username', 'email', 'first_name', 'get_is_confirmed')
    list_select_related = ('profile', 'status')

    def get_is_confirmed(self, instance):
        return instance.status.is_confirmed

    get_is_confirmed.short_description = 'Is confirmed'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
