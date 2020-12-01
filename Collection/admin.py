from django.contrib import admin

from .models import Collection

admin.site.site_header = "Credy Dashboard"
admin.site.site_title = "Admin Panel"
admin.site.register(Collection)
