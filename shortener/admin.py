from django.contrib import admin
from .models import URL

class URLAdmin(admin.ModelAdmin):
    list_display = ('link', 'uuid', 'time', 'ip_address', 'os', 'device')

admin.site.register(URL, URLAdmin)
