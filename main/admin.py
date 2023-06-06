from django.contrib import admin
from .models import (contactus, team)
# Register your models here.



class contactusAdmin(admin.ModelAdmin):
    list_display = ('client_email','client_name', 'client_message')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','designation', 'info','facebook', 'instagram','dropbox', 'twitter', 'img')
    
admin.site.register(contactus, contactusAdmin)
admin.site.register(team, TeamAdmin)