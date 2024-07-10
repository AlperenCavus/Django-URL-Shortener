from django.contrib import admin
from .models import URL, UserAccess

class URLAdmin(admin.ModelAdmin):
    list_display = ('link', 'uuid', 'short_uuid', 'time')

class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('url', 'ip_address', 'os', 'device', 'time', 'clicks')

admin.site.register(URL, URLAdmin)
admin.site.register(UserAccess, UserAccessAdmin)
