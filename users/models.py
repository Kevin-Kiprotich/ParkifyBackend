from django.contrib.gis.db import models


# Create your models here.
class Parks(models.Model):
    id = models.IntegerField(null=False)
    name= models.CharField(max_length=30, null=False, primary_key=True)
    capacity=models.IntegerField(default=0, null=False)
    booked=models.IntegerField(default=0, null=False)
    available_spaces= models.IntegerField(default=0, null=False)

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Parks"

class ParkingSlots(models.Model):
    id = models.CharField(max_length=30, null=False, primary_key=True)
    name = models.ForeignKey(Parks, on_delete=models.CASCADE)
    slot_no=models.IntegerField(null=False)
    is_parked=models.BooleanField(default=False)
    geometry = models.MultiPolygonField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural = "Parking Slots"