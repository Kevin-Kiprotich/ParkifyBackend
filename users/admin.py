from django.contrib import admin
from .models import Parks
# Register your models here.

class ParksAdmin(admin.ModelAdmin):
    list_display = ['id','name','capacity','booked','available_spaces']

admin.site.register(Parks, ParksAdmin)