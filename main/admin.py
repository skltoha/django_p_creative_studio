from django.contrib import admin
from .models import (contactus, team, clientsay)
# Register your models here.


class contactusAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'client_name', 'client_message')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'info', 'facebook',
                    'instagram', 'dropbox', 'twitter', 'img')


class clientsayAdmin(admin.ModelAdmin):
    list_display = ('name', 'comments', 'img')



admin.site.register(contactus, contactusAdmin)
admin.site.register(team, TeamAdmin)
admin.site.register(clientsay, clientsayAdmin)

