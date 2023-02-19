#!/usr/bin/python3

"""
Author: Dickson Agbemazi

Description: 
"""

from collections import namedtuple
from time import sleep
import json
from ev_db import db_defaults
from ev_data_insertion import insert_and_fetch_id


def fetch_data():
    
    with open("rows.json") as file:
        ev_data = file.read()

        js_ev_data = json.loads(ev_data)
        data = js_ev_data["data"]   
        
        for row in data:
            if (data.index(row) % 10) == 0:
                sleep(5)
            tuple_row = tuple(row[8:len(row)-3])

            ElectricVehicle = namedtuple("ElectricVehicle", 
            ["vin", "county", "city", "state", "zip_code", 
            "model_year", "make", "model", "ev_type", 
            "cafv_type", "electric_range", "base_msrp", 
            "legis_district", "dol_id", "geocode", "electric_utility", "census_tract"])     

            ev = ElectricVehicle(*tuple_row) # Unpack tuple into namedtuple.
            
            insert_and_fetch_id(ev)
            

if __name__ == "__main__":
    db_defaults()
    fetch_data()