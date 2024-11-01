from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Parks

parks_mapping = {
    "id":"id",
    "name":"Name",
    "capacity":"capacity",
    "available_spaces":"available_spaces",
    "mpoly":"MULTIPOLYGON"
}

parks_shp = "D:/Projects/Django_Projects/parkify/ParkifyApi/users/parks.geojson"


def run(verbose=True):
    lm=LayerMapping(Parks, parks_shp, parks_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)