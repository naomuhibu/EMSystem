import os
from django.contrib.gis.utils import LayerMapping
from EMSystem.models import NZregionalcouncil

# Model and shapefile column mapping
NZregionalcouncil_mapping = {
    'regc2023_v' : 'Regc2023_v',
    'regc2023_1' :'Regc2023_1',
    'regc2023_2' : 'Regc2023_2',
    'land_area_field' : 'Land_area_field',
    'area_sq_km' : 'Area_sq_km',
    'shape_leng' : 'Shape_leng',
    'geom' : 'POLYGON',
}
# shapefile
NZregionalcouncil_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'static', 'regional-council-2023-generalised.shp'),
)

def run(verbose=True):
    lm = LayerMapping(NZregionalcouncil, NZregionalcouncil_shp, NZregionalcouncil_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)