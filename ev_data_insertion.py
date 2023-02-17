#!/usr/bin/python3

"""This program accepts a named tuple, unpacks,
inserts and fetchs ID of inserts into a DB.

"""

import sqlite3

conn = sqlite3.connect("ev_data.sqlite")
cur = conn.cursor()


def insert_and_fetch_id(ev:tuple):

    cur.execute("INSERT OR IGNORE INTO City(city) VALUES ( ? )", (ev.city,))
    cur.execute("SELECT id FROM City where city = ?;", (ev.city,))
    city_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Vin_1_10(vin_1_10) VALUES ( ? )", (ev.vin,))
    cur.execute("SELECT id FROM City where city = ?;", (ev.vin,))
    vin_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO County(county)) VALUES ( ? )", (ev.county,)) 
    cur.execute("SELECT id FROM County where county = ?;", (ev.county,))
    county_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO State(state) VALUES ( ? )", (ev.state,))  
    cur.execute("SELECT id FROM City where city = ?;", (ev.state,))
    state_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO ZipCode(zip_code) VALUES ( ? )", (ev.zip_code,))   
    cur.execute("SELECT id FROM ZipCode where zip_code = ?;", (ev.zip_code,))
    zip_code_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO ModelYear(model_year) VALUES ( ? )", (ev.model_year,))
    cur.execute("SELECT id FROM ModelYear where model_year = ?;", (ev.model_year,))
    model_year_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Model(model) VALUES ( ? )", (ev.model,))
    cur.execute("SELECT id FROM Model where model = ?;", (ev.model,))
    model_id = cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Make(make) VALUES ( ? )", (ev.make,))
    cur.execute("SELECT id FROM Make where make = ?;", (ev.make,))
    make_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO EV_Type(ev_type) VALUES ( ? )", (ev.ev_type,))
    cur.execute("SELECT id FROM EV_Type where ev_type = ?;", (ev.ev_type,))
    ev_type_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO CAFV_Type(cafv_type) VALUES ( ? )", (ev.cafv_type,))
    cur.execute("SELECT id FROM CAFV_Type where cafv_type = ?;", (ev.cafv_type,))
    cafv_type_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO ElectricRange(electric_range) VALUES ( ? )", (ev.electric_range,))
    cur.execute("SELECT id FROM ElectricRange where electric_range = ?;", (ev.electric_range,))
    electric_range_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO BaseMSRP(base_msrp) VALUES ( ? )", (ev.base_msrp,))
    cur.execute("SELECT id FROM BaseMSRP where base_msrp = ?;", (ev.base_msrp,))
    base_msrp_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO DOL_VehicleID(dol_vehicle) VALUES ( ? )", (ev.dol_id,))
    cur.execute("SELECT id FROM DOL_VehicleID where dol_vehicle = ?;", (ev.dol_id,))
    dol_vehicle_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO LegislativeDistrict(legis_district) VALUES ( ? )", (ev.legis_district,))
    cur.execute("SELECT id FROM LegislativeDistrict where legis_district = ?;", (ev.legis_district,))
    legis_district_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO GeocodedColumn(geocode_column) VALUES ( ? )", (ev.geocode,))
    cur.execute("SELECT id FROM GeocodedColumn where geocoded_column = ?;", (ev.geocode,))
    geocoded_column_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO ElectricUtility(electric_utility) VALUES ( ? )", (ev.electric_utility,))
    cur.execute("SELECT id FROM ElectricUtility where electric_utility = ?;", (ev.electric_utility,))
    electric_utility_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO CensusTract(census_tract_2020) VALUES ( ? )", (ev.census_tract_2020,))
    cur.execute("SELECT id FROM CensusTract where census_tract_2020 = ?;", (ev.census_tract_2020,))
    census_tract_2020_id = cur.fetchone()[0]

    row_ids = [vin_id, county_id, city_id, state_id, 
    zip_code_id, model_year_id, make_id, model_id, 
    ev_type_id, cafv_type_id, electric_range_id, base_msrp_id, 
    legis_district_id, dol_vehicle_id, geocoded_column_id, 
    electric_utility_id, census_tract_2020_id]


    cur.executemany("""INSERT OR IGNORE INTO Electric_Vehicles
    (   vin_1_10_id,
        county_id,
        city_id,
        state_id,
        zip_code_id,
        model_year_id,
        make_id,
        model_id,
        ev_type_id,
        cafv_type_id,
        electric_range_id,
        base_msrp_id,
        legis_district_id,
        dol_vehicle_id,
        geocoded_column_id,
        electric_utility_id,
        census_tract_2020_id) 
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )""", 
        (row_ids))
   
    conn.commit()