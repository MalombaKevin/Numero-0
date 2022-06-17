from django.contrib import admin

from numeroapp.models import numero_Profile, numero_Project

# Register your models here.
admin.site.register(numero_Profile)
admin.site.register(numero_Project)