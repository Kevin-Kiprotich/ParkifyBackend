from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ParkingSlots, Parks


@receiver(post_save, sender=ParkingSlots)
@receiver(post_delete, sender=ParkingSlots)
def update_park_on_slot_change(sender, instance, **kwargs):
    #get the related park
    park = instance.name

    # get the counts of all parking slots to update the parks info
    total_slots = ParkingSlots.objects.filter(name=park).count()
    booked_slots = ParkingSlots.objects.filter(name=park, is_parked=True).count()
    available_slots = total_slots - booked_slots

    #update the park's fields
    park.capacity = total_slots
    park.booked = booked_slots
    park.available_spaces = available_slots
    park.save()