from django.contrib import admin
from .models import Parks, ParkingSlots
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class ParksAdmin(LeafletGeoAdmin):
    list_display = ['id','name','capacity','booked','available_spaces']

class ParkingSlotsAdmin(LeafletGeoAdmin):
    list_display = ['id','name','slot_no','is_parked']

admin.site.register(Parks, ParksAdmin)
admin.site.register(ParkingSlots, ParkingSlotsAdmin)