#!/usr/bin/python

import json
import geo_helper

f = open('LHR11_actual.geojson', 'r')
geojson = json.load(f)
f.close()

for feature in geojson['features']:
    coords = []
    for coord in feature['geometry']['coordinates']:

        osgb_coord = geo_helper.turn_eastingnorthing_into_osgb36(coord[0], coord[1])
        osgb_xyz = geo_helper.turn_llh_into_xyz(osgb_coord[0], osgb_coord[1], 0, 'osgb')
        wgs_xyz = geo_helper.turn_xyz_into_other_xyz(osgb_xyz[0],osgb_xyz[1],osgb_xyz[2],'osgb','wgs84')
        wgs_coord = geo_helper.turn_xyz_into_llh(wgs_xyz[0],wgs_xyz[1],wgs_xyz[2],'wgs84')

        coords.append([wgs_coord[1], wgs_coord[0], 0])
    
    feature['geometry']['coordinates'] = coords

f = open('LHR11_actual_wgs84.geojson', 'w')
json.dump(geojson, f, indent=4)
f.close()
    