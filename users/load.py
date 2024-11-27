from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Parks, ParkingSlots
from django.contrib.gis.geos import GEOSGeometry

parks_mapping = {
    "id":"id",
    "name":"name",
    "capacity":"capacity",
    "available_spaces":"available",
    "mpoly":"MULTIPOLYGON"
}

parks_shp = "D:/DevProjects/DjangoApps/ParkifyBackend/users/parks.geojson"
parking_slots_shp = "D:/DevProjects/DjangoApps/ParkifyBackend/users/parking_slots.geojson"

def run(verbose=True):
    lm=LayerMapping(Parks, parks_shp, parks_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def save_parking_slots(verbose=True):
    import json

    # Load parking slots GeoJSON
    with open(parking_slots_shp, 'r') as f:
        data = json.load(f)

    for feature in data["features"]:
        slot_properties = feature["properties"]
        slot_geometry = feature["geometry"]

        # Get the park name from the parking slot data
        park_name = slot_properties["name"]

        # Fetch the corresponding Parks instance
        try:
            park_instance = Parks.objects.get(name=park_name)
        except Parks.DoesNotExist:
            print(f"Park with name '{park_name}' does not exist. Skipping.")
            continue

        # Parse the geometry
        try:
            geometry = GEOSGeometry(json.dumps(slot_geometry))
        except Exception as e:
            print(f"Error parsing geometry for slot ID {slot_properties['id']}: {e}")
            continue

        # Create or update the ParkingSlot instance
        parking_slot = ParkingSlots(
            id=slot_properties["id"],
            name=park_instance,
            slot_no=slot_properties["slot_no"],
            is_parked=False,
            geometry=geometry,
        )
        parking_slot.save()

        print(f"Saved: {slot_properties['id']}")

    if verbose:
        print(f"Parking slots with geometry from {parking_slots_shp} have been successfully saved.")