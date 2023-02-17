#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect("ev_data.sqlite")
cur = conn.cursor()


def db_defaults():

    cur.executescript("""

    CREATE TABLE IF NOT EXISTS Electric_Vehicles (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        vin_1_10_id INTEGER,
        county_id INTEGER,
        city_id INTEGER,
        state_id INTEGER,
        zip_code_id INTEGER
        model_year_id INTEGER
        make_id INTEGER
        model_id INTEGER
        ev_type_id INTEGER
        cafv_type_id INTEGER
        electric_range_id INTEGER
        base_msrp_id INTEGER
        legis_district_id INTEGER
        dol_vehicle_id INTEGER
        geocoded_column_id INTEGER
        electric_utility_id INTEGER
        census_tract_2020_id INTEGER
    );

    CREATE TABLE IF NOT EXISTS Vin_1_10 (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        vin_1_10 INTEGER
    );

    CREATE TABLE IF NOT EXISTS County (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        county TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS City (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        city TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS State (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        state TEXT UNIQUE
    );
    CREATE TABLE IF NOT EXISTS ZipCode (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        zip_code INTEGER UNIQUE    
    );

    CREATE TABLE IF NOT EXISTS ModelYear (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        model_year INTEGER UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Model (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        model TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Make (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        make TEXT UNIQUE
    );    


    CREATE TABLE IF NOT EXISTS EV_Type (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,      
        ev_type TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS CAFV_Type (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        cafv_type TEXT UNIQUE
    );
    CREATE TABLE IF NOT EXISTS ElectricRange (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,       
        electric_range INTEGER
    );
    CREATE TABLE IF NOT EXISTS BaseMSRP (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        base_msrp INTEGER
    );
    CREATE TABLE IF NOT EXISTS LegislativeDistrict (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        legis_district INTEGER
    );
    CREATE TABLE IF NOT EXISTS DOL_VehicleID (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,     
        dol_vehicle INTEGER
    );
    CREATE TABLE IF NOT EXISTS GeocodedColumn (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        geoceded_column TEXT UNIQUE  
    );
    CREATE TABLE IF NOT EXISTS ElectricUtility (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        electric_utility TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS CensusTract (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,       
        census_tract_2020 INTEGER
    );
   
    """)