from .models import Parks, ParkingSlots


def run():
    for park in Parks.objects.all():
        # get the counts of all parking slots to update the parks info
        total_slots = ParkingSlots.objects.filter(name=park).count()
        booked_slots = ParkingSlots.objects.filter(name=park, is_parked=True).count()
        available_slots = total_slots - booked_slots

        #update the park's fields
        park.capacity = total_slots
        park.booked = booked_slots
        park.available_spaces = available_slots
        park.save()


        print(f"updated: {park.name}")        

