"""
This module is responsible for setting up and querying the database.
"""

"""
Task 22 - 26: Write suitable functions to query the database as follows:

TASK 22: Setup database
TASK 23: Retrieve the names of all (unique) countries in alphabetical order
TASK 24: Retrieve the number of confirmed cases, deaths and recoveries for a specified record / serial number.
TASK 25: Retrieve information for the top 5 countries for confirmed cases
TASK 26: Retrieve information for the top 5 countries for death for specific observation dates

The function for setting up the database should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database
"""

# TO DO: Your code here
#TASK 22: Setup database
import sqlite3
import tui

def setup_database(list_of_records):
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    sql = """
    BEGIN TRANSACTION;
    CREATE TABLE IF NOT EXISTS "dates" (
        "dates_id"	INTEGER DEFAULT 1 UNIQUE,
        "observation_date"	TEXT NOT NULL,
        "last_update"	TEXT NOT NULL,
        PRIMARY KEY("dates_id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "countries_regions" (
        "country_region_id"	INTEGER DEFAULT 1 UNIQUE,
        "country_region"	TEXT NOT NULL,
        PRIMARY KEY("country_region_id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "provinces_states" (
        "province_state_id"	INTEGER DEFAULT 1 UNIQUE,
        "province_state"	TEXT,
        "country_region_id"	INTEGER,
        FOREIGN KEY("country_region_id") REFERENCES "countries_regions"("country_region_id"),
        PRIMARY KEY("province_state_id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "records" (
        "record_id"	INTEGER DEFAULT 1 UNIQUE,
        "sno"	INTEGER NOT NULL UNIQUE,
        "country_region_id"	INTEGER,
        "dates_id"	INTEGER,
        FOREIGN KEY("dates_id") REFERENCES "dates"("dates_id"),
        FOREIGN KEY("country_region_id") REFERENCES "countries_regions"("country_region_id"),
        PRIMARY KEY("record_id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "statistics" (
        "statistics_id"	INTEGER DEFAULT 1 UNIQUE,
        "confirmed"	INTEGER NOT NULL,
        "deaths"	INTEGER NOT NULL,
        "recovered"	INTEGER NOT NULL,
        "record_id"	INTEGER,
        FOREIGN KEY("record_id") REFERENCES "records"("record_id"),
        PRIMARY KEY("statistics_id" AUTOINCREMENT)
    );
    COMMIT;
    """
    cursor.executescript(sql)
    db.commit()

    ####### PREPARE THE DATA THAT NEEDS TO BE INSERTED IN THE TABELS

    # prepare the data for the table: countries_regions
    countries = []
    for rec in range(len(list_of_records)):
        # print(list_of_records[rec][3])
        countries.append(list_of_records[rec][3])
    countries = list(dict.fromkeys(countries))
    # print(countries)

    # prepare the data for the table: dates
    dates = []
    for rec in range(len(list_of_records)):
        date = []
        date.append(list_of_records[rec][1])
        date.append(list_of_records[rec][4])
        dates.append(date)
    # removing duplicates from the list of lists
    dates_unique = []
    for date in dates:
        if date not in dates_unique:
            dates_unique.append(date)
    # print(dates_unique)

    # prepare the data for the table: provinces_states
    provinces_states = []
    for rec in range(len(list_of_records)):
        province_country = []
        province_country.append(list_of_records[rec][2])
        province_country.append(list_of_records[rec][3])
        provinces_states.append(province_country)

    # removing duplicates from the list of lists
    unique_provinces_states_list = []
    for p in provinces_states:
        if p not in unique_provinces_states_list:
            unique_provinces_states_list.append(p)
    # print(unique_provinces_states_list)

    # prepare the data for the table: records
    records = []
    for rec in range(len(list_of_records)):
        record = []
        record.append(list_of_records[rec][0])
        record.append(list_of_records[rec][3])
        record.append(list_of_records[rec][1])
        record.append(list_of_records[rec][4])
        records.append(record)
    # removing duplicates, although it should be none (but in case there will be in the future)
    unique_records_list = []
    for r in records:
        if r not in unique_records_list:
            unique_records_list.append(r)
    # print(unique_records_list)

    # prepare the data for the table: statistics
    statistics = []
    for rec in range(len(list_of_records)):
        stat = []
        stat.append(list_of_records[rec][5])
        stat.append(list_of_records[rec][6])
        stat.append(list_of_records[rec][7])
        stat.append(list_of_records[rec][0])
        statistics.append(stat)
    # removing duplicates, although it should be none (but in case there will be in the future)
    unique_statistics_list = []
    for s in statistics:
        if s not in unique_statistics_list:
            unique_statistics_list.append(s)
    # print(unique_statistics_list)

    ##### GETTING THE PREPARED DATA INTO THE TABLES
    # insert the unique values of country_region into the countries_regions table
    for con in countries:
        value = [con]
        sql_query = f"INSERT INTO countries_regions (country_region) VALUES (?);"
        cursor.execute(sql_query, value)
        db.commit()
    # check the insert
    # sql_query = "SELECT * FROM countries_regions"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print(all_records)

    # insert the unique values of obs_date and last_update into the dates table
    for dat in dates_unique:
        values = [dat[0], dat[1]]
        sql_query = "INSERT INTO dates (observation_date, last_update) VALUES (?, ?);"
        cursor.execute(sql_query, values)
        db.commit()
    # check the insert
    # sql_query = "SELECT * FROM dates"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print(all_records)

    # insert the values in the table provinces_states
    for prov in unique_provinces_states_list:
        values = [prov[0], prov[1]]
        sql_query="INSERT INTO provinces_states (province_state, country_region_id) VALUES " \
                  "(?, (SELECT countries_regions.country_region_id FROM countries_regions WHERE countries_regions.country_region=?));"
        cursor.execute(sql_query, values)
        db.commit()

    # insert the values in the table records
    for rec in unique_records_list:
        values = [rec[0], rec[1], rec[2], rec[3]]
        sql_query = "INSERT INTO records (sno, country_region_id, dates_id) VALUES (?, (SELECT countries_regions.country_region_id FROM countries_regions WHERE countries_regions.country_region=?), (SELECT dates.dates_id FROM dates WHERE dates.observation_date=? AND dates.last_update=?));"
        cursor.execute(sql_query, values)
        db.commit()

    # insert the values in the table statistics
    for st in unique_statistics_list:
        values=[st[0], st[1], st[2], st[3]]
        sql_query="INSERT INTO statistics (confirmed, deaths, recovered, record_id) VALUES (?, ?, ?, (SELECT records.record_id FROM records WHERE records.sno = ?));"
        cursor.execute(sql_query, values)
        db.commit()
    # FINAL CHECK to see if all the data has inserted
    # sql_query = "SELECT * FROM countries_regions"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print("SELECT * FROM countries_regions")
    # print(all_records)
    #
    # sql_query = "SELECT * FROM provinces_states"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print("SELECT * FROM provinces_states")
    # print(all_records)
    #
    # sql_query = "SELECT * FROM dates"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print("SELECT * FROM dates")
    # print(all_records)
    #
    # sql_query = "SELECT * FROM records"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print("SELECT * FROM records")
    # print(all_records)
    #
    # sql_query = "SELECT * FROM statistics"
    # cursor.execute(sql_query)
    # all_records = cursor.fetchall()
    # print("SELECT * FROM statistics")
    # print(all_records)
    db.close()

#setup_database([['1', '01/22/2020', 'Anhui', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['2', '01/22/2020', 'Beijing', 'Mainland China', '1/22/2020 17:00', '14', '0', '0'], ['3', '01/22/2020', 'Chongqing', 'Mainland China', '1/22/2020 17:00', '6', '0', '0'], ['4', '01/22/2020', 'Fujian', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['5', '01/22/2020', 'Gansu', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['6', '01/22/2020', 'Guangdong', 'Mainland China', '1/22/2020 17:00', '26', '0', '0'], ['7', '01/22/2020', 'Guangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['8', '01/22/2020', 'Guizhou', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['9', '01/22/2020', 'Hainan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['10', '01/22/2020', 'Hebei', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['11', '01/22/2020', 'Heilongjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['12', '01/22/2020', 'Henan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['13', '01/22/2020', 'Hong Kong', 'Hong Kong', '1/22/2020 17:00', '0', '0', '0'], ['14', '01/22/2020', 'Hubei', 'Mainland China', '1/22/2020 17:00', '444', '17', '28'], ['15', '01/22/2020', 'Hunan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['16', '01/22/2020', 'Inner Mongolia', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['17', '01/22/2020', 'Jiangsu', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['18', '01/22/2020', 'Jiangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['19', '01/22/2020', 'Jilin', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['20', '01/22/2020', 'Liaoning', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['21', '01/22/2020', 'Macau', 'Macau', '1/22/2020 17:00', '1', '0', '0'], ['22', '01/22/2020', 'Ningxia', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['23', '01/22/2020', 'Qinghai', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['24', '01/22/2020', 'Shaanxi', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['25', '01/22/2020', 'Shandong', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['26', '01/22/2020', 'Shanghai', 'Mainland China', '1/22/2020 17:00', '9', '0', '0'], ['27', '01/22/2020', 'Shanxi', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['28', '01/22/2020', 'Sichuan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['29', '01/22/2020', 'Taiwan', 'Taiwan', '1/22/2020 17:00', '1', '0', '0'], ['30', '01/22/2020', 'Tianjin', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['31', '01/22/2020', 'Tibet', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['32', '01/22/2020', 'Washington', 'US', '1/22/2020 17:00', '1', '0', '0'], ['33', '01/22/2020', 'Xinjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['34', '01/22/2020', 'Yunnan', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['35', '01/22/2020', 'Zhejiang', 'Mainland China', '1/22/2020 17:00', '10', '0', '0'], ['36', '01/22/2020', '', 'Japan', '1/22/2020 17:00', '2', '0', '0'], ['37', '01/22/2020', '', 'Thailand', '1/22/2020 17:00', '4', '0', '2'], ['38', '01/22/2020', '', 'South Korea', '1/22/2020 17:00', '1', '0', '0'], ['39', '01/22/2020', 'Unknown', 'China', '1/22/2020 17:00', '0', '0', '0'], ['40', '01/22/2020', '', 'Kiribati', '1/22/2020 17:00', '0', '0', '0'], ['41', '01/23/2020', 'Anhui', 'Mainland China', '1/23/20 17:00', '9', '0', '0'], ['42', '01/23/2020', 'Beijing', 'Mainland China', '1/23/20 17:00', '22', '0', '0'], ['43', '01/23/2020', 'Chongqing', 'Mainland China', '1/23/20 17:00', '9', '0', '0'], ['44', '01/23/2020', 'Fujian', 'Mainland China', '1/23/20 17:00', '5', '0', '0'], ['45', '01/23/2020', 'Gansu', 'Mainland China', '1/23/20 17:00', '2', '0', '0'], ['46', '01/23/2020', 'Guangdong', 'Mainland China', '1/23/20 17:00', '32', '0', '2'], ['47', '01/23/2020', 'Guangxi', 'Mainland China', '1/23/20 17:00', '5', '0', '0'], ['48', '01/23/2020', 'Guizhou', 'Mainland China', '1/23/20 17:00', '3', '0', '0'], ['49', '01/23/2020', 'Hainan', 'Mainland China', '1/23/20 17:00', '5', '0', '0'], ['50', '01/23/2020', 'Hubei', 'Mainland China', '1/23/20 17:00', '444', '17', '28'], ['51', '01/23/2020', 'Heilongjiang', 'Mainland China', '1/23/20 17:00', '2', '0', '0'], ['52', '01/23/2020', 'Henan', 'Mainland China', '1/23/20 17:00', '5', '0', '0'], ['53', '01/23/2020', 'Hong Kong', 'Hong Kong', '1/23/20 17:00', '2', '0', '0'], ['54', '01/23/2020', 'Hubei', 'Mainland China', '1/23/20 17:00', '444', '17', '28'], ['55', '01/23/2020', 'Hunan', 'Mainland China', '1/23/20 17:00', '9', '0', '0'], ['56', '01/23/2020', 'Inner Mongolia', 'Mainland China', '1/23/20 17:00', '0', '0', '0'], ['57', '01/23/2020', 'Jiangsu', 'Mainland China', '1/23/20 17:00', '5', '0', '0'], ['58', '01/23/2020', 'Jiangxi', 'Mainland China', '1/23/20 17:00', '7', '0', '0'], ['59', '01/23/2020', 'Jilin', 'Mainland China', '1/23/20 17:00', '1', '0', '0'], ['60', '01/23/2020', 'Liaoning', 'Mainland China', '1/23/20 17:00', '3', '0', '0'], ['61', '01/23/2020', 'Macau', 'Macau', '1/23/20 17:00', '2', '0', '0'], ['62', '01/23/2020', 'Ningxia', 'Mainland China', '1/23/20 17:00', '1', '0', '0'], ['63', '01/23/2020', 'Qinghai', 'Mainland China', '1/23/20 17:00', '0', '0', '0'], ['64', '01/23/2020', 'Shaanxi', 'Mainland China', '1/23/20 17:00', '3', '0', '0'], ['65', '01/23/2020', 'Shandong', 'Mainland China', '1/23/20 17:00', '6', '0', '0'], ['66', '01/23/2020', 'Shanghai', 'Mainland China', '1/23/20 17:00', '16', '0', '0'], ['67', '01/23/2020', 'Shanxi', 'Mainland China', '1/23/20 17:00', '1', '0', '0'], ['68', '01/23/2020', 'Sichuan', 'Mainland China', '1/23/20 17:00', '8', '0', '0'], ['69', '01/23/2020', 'Taiwan', 'Taiwan', '1/23/20 17:00', '1', '0', '0'], ['70', '01/23/2020', 'Tianjin', 'Mainland China', '1/23/20 17:00', '4', '0', '0'], ['71', '01/23/2020', 'Tibet', 'Mainland China', '1/23/20 17:00', '0', '0', '0'], ['72', '01/23/2020', 'Washington', 'US', '1/23/20 17:00', '1', '0', '0'], ['73', '01/23/2020', 'Xinjiang', 'Mainland China', '1/23/20 17:00', '2', '0', '0'], ['74', '01/23/2020', 'Yunnan', 'Mainland China', '1/23/20 17:00', '2', '0', '0'], ['75', '01/23/2020', 'Zhejiang', 'Mainland China', '1/23/20 17:00', '27', '0', '0'], ['76', '01/23/2020', '', 'Japan', '1/23/20 17:00', '1', '0', '0'], ['77', '01/23/2020', '', 'Thailand', '1/23/20 17:00', '4', '0', '2'], ['78', '01/23/2020', '', 'South Korea', '1/23/20 17:00', '1', '0', '0'], ['79', '01/23/2020', '', 'Singapore', '1/23/20 17:00', '1', '0', '0'], ['80', '01/23/2020', '', 'Philippines', '1/23/20 17:00', '0', '0', '0'], ['81', '01/23/2020', '', 'Malaysia', '1/23/20 17:00', '0', '0', '0'], ['82', '01/23/2020', '', 'Vietnam', '1/23/20 17:00', '2', '0', '0'], ['83', '01/23/2020', '', 'Australia', '1/23/20 17:00', '0', '0', '0'], ['84', '01/23/2020', '', 'Mexico', '1/23/20 17:00', '0', '0', '0'], ['85', '01/23/2020', '', 'Brazil', '1/23/20 17:00', '0', '0', '0'], ['86', '01/23/2020', '', 'Colombia', '1/23/20 17:00', '0', '0', '0'], ['87', '01/23/2020', 'Unknown', 'China', '1/23/20 17:00', '0', '0', '0'], ['88', '01/23/2020', '', 'Kiribati', '1/23/20 17:00', '0', '0', '0'], ['89', '01/24/2020', 'Hubei', 'Mainland China', '1/24/20 17:00', '549', '24', '31'], ['90', '01/24/2020', 'Guangdong', 'Mainland China', '1/24/20 17:00', '53', '0', '2'], ['91', '01/24/2020', 'Zhejiang', 'Mainland China', '1/24/20 17:00', '43', '0', '1'], ['92', '01/24/2020', 'Beijing', 'Mainland China', '1/24/20 17:00', '36', '0', '1'], ['93', '01/24/2020', 'Chongqing', 'Mainland China', '1/24/20 17:00', '27', '0', '0'], ['94', '01/24/2020', 'Hunan', 'Mainland China', '1/24/20 17:00', '24', '0', '0'], ['95', '01/24/2020', 'Guangxi', 'Mainland China', '1/24/20 17:00', '23', '0', '0'], ['96', '01/24/2020', 'Shanghai', 'Mainland China', '1/24/20 17:00', '20', '0', '1'], ['97', '01/24/2020', 'Jiangxi', 'Mainland China', '1/24/20 17:00', '18', '0', '0'], ['98', '01/24/2020', 'Sichuan', 'Mainland China', '1/24/20 17:00', '15', '0', '0'], ['99', '01/24/2020', 'Shandong', 'Mainland China', '1/24/20 17:00', '15', '0', '0'], ['100', '01/24/2020', 'Anhui', 'Mainland China', '1/24/20 17:00', '15', '0', '0'], ['101', '01/24/2020', 'Fujian', 'Mainland China', '1/24/20 17:00', '10', '0', '0'], ['102', '01/24/2020', 'Henan', 'Mainland China', '1/24/20 17:00', '9', '0', '0'], ['103', '01/24/2020', 'Jiangsu', 'Mainland China', '1/24/20 17:00', '9', '0', '0'], ['104', '01/24/2020', 'Hainan', 'Mainland China', '1/24/20 17:00', '8', '0', '0'], ['105', '01/24/2020', 'Tianjin', 'Mainland China', '1/24/20 17:00', '8', '0', '0'], ['106', '01/24/2020', 'Yunnan', 'Mainland China', '1/24/20 17:00', '5', '0', '0'], ['107', '01/24/2020', 'Shaanxi', 'Mainland China', '1/24/20 17:00', '5', '0', '0'], ['108', '01/24/2020', 'Heilongjiang', 'Mainland China', '1/24/20 17:00', '4', '1', '0'], ['109', '01/24/2020', 'Liaoning', 'Mainland China', '1/24/20 17:00', '4', '0', '0'], ['110', '01/24/2020', 'Guizhou', 'Mainland China', '1/24/20 17:00', '3', '0', '0'], ['111', '01/24/2020', 'Jilin', 'Mainland China', '1/24/20 17:00', '3', '0', '0'], ['112', '01/24/2020', 'Taiwan', 'Taiwan', '1/24/20 17:00', '3', '0', '0'], ['113', '01/24/2020', 'Ningxia', 'Mainland China', '1/24/20 17:00', '2', '0', '0'], ['114', '01/24/2020', 'Hong Kong', 'Hong Kong', '1/24/20 17:00', '2', '0', '0'], ['115', '01/24/2020', 'Macau', 'Macau', '1/24/20 17:00', '2', '0', '0'], ['116', '01/24/2020', 'Hebei', 'Mainland China', '1/24/20 17:00', '2', '1', '0'], ['117', '01/24/2020', 'Gansu', 'Mainland China', '1/24/20 17:00', '2', '0', '0'], ['118', '01/24/2020', 'Xinjiang', 'Mainland China', '1/24/20 17:00', '2', '0', '0'], ['119', '01/24/2020', 'Shanxi', 'Mainland China', '1/24/20 17:00', '1', '0', '0'], ['120', '01/24/2020', 'Inner Mongolia', 'Mainland China', '1/24/20 17:00', '1', '0', '0'], ['121', '01/24/2020', 'Qinghai', 'Mainland China', '1/24/20 17:00', '0', '0', '0'], ['122', '01/24/2020', 'Washington', 'US', '1/24/20 17:00', '1', '0', '0'], ['123', '01/24/2020', 'Chicago', 'US', '1/24/20 17:00', '1', '0', '0'], ['124', '01/24/2020', '', 'Japan', '1/24/20 17:00', '2', '0', '0'], ['125', '01/24/2020', '', 'Thailand', '1/24/20 17:00', '5', '0', '3'], ['126', '01/24/2020', '', 'South Korea', '1/24/20 17:00', '2', '0', '0'], ['127', '01/24/2020', '', 'Singapore', '1/24/20 17:00', '3', '0', '0'], ['128', '01/24/2020', '', 'Vietnam', '1/24/20 17:00', '2', '0', '0'], ['129', '01/24/2020', '', 'France', '1/24/20 17:00', '2', '0', '0'], ['130', '01/24/2020', 'Unknown', 'China', '1/24/20 17:00', '0', '0', '0'], ['131', '01/24/2020', '', 'Kiribati', '1/24/20 17:00', '0', '0', '0'], ['132', '01/25/2020', 'Hubei', 'Mainland China', '1/25/20 17:00', '761', '40', '32'], ['133', '01/25/2020', 'Guangdong', 'Mainland China', '1/25/20 17:00', '78', '0', '2'], ['134', '01/25/2020', 'Zhejiang', 'Mainland China', '1/25/20 17:00', '62', '0', '1'], ['135', '01/25/2020', 'Chongqing', 'Mainland China', '1/25/20 17:00', '57', '0', '0'], ['136', '01/25/2020', 'Hunan', 'Mainland China', '1/25/20 17:00', '43', '0', '0'], ['137', '01/25/2020', 'Beijing', 'Mainland China', '1/25/20 17:00', '41', '0', '2'], ['138', '01/25/2020', 'Anhui', 'Mainland China', '1/25/20 17:00', '39', '0', '0'], ['139', '01/25/2020', 'Shanghai', 'Mainland China', '1/25/20 17:00', '33', '0', '1'], ['140', '01/25/2020', 'Henan', 'Mainland China', '1/25/20 17:00', '32', '0', '0'], ['141', '01/25/2020', 'Sichuan', 'Mainland China', '1/25/20 17:00', '28', '0', '0'], ['142', '01/25/2020', 'Shandong', 'Mainland China', '1/25/20 17:00', '27', '0', '0'], ['143', '01/25/2020', 'Guangxi', 'Mainland China', '1/25/20 17:00', '23', '0', '0'], ['144', '01/25/2020', 'Hainan', 'Mainland China', '1/25/20 17:00', '19', '0', '0'], ['145', '01/25/2020', 'Jiangxi', 'Mainland China', '1/25/20 17:00', '18', '0', '0'], ['146', '01/25/2020', 'Fujian', 'Mainland China', '1/25/20 17:00', '18', '0', '0'], ['147', '01/25/2020', 'Jiangsu', 'Mainland China', '1/25/20 17:00', '18', '0', '1'], ['148', '01/25/2020', 'Liaoning', 'Mainland China', '1/25/20 17:00', '17', '0', '0'], ['149', '01/25/2020', 'Shaanxi', 'Mainland China', '1/25/20 17:00', '15', '0', '0'], ['150', '01/25/2020', 'Yunnan', 'Mainland China', '1/25/20 17:00', '11', '0', '0'], ['151', '01/25/2020', 'Tianjin', 'Mainland China', '1/25/20 17:00', '10', '0', '0'], ['152', '01/25/2020', 'Heilongjiang', 'Mainland China', '1/25/20 17:00', '9', '1', '0'], ['153', '01/25/2020', 'Hebei', 'Mainland China', '1/25/20 17:00', '8', '1', '0'], ['154', '01/25/2020', 'Inner Mongolia', 'Mainland China', '1/25/20 17:00', '7', '0', '0'], ['155', '01/25/2020', 'Shanxi', 'Mainland China', '1/25/20 17:00', '6', '0', '0'], ['156', '01/25/2020', 'Hong Kong', 'Hong Kong', '1/25/20 17:00', '5', '0', '0'], ['157', '01/25/2020', 'Guizhou', 'Mainland China', '1/25/20 17:00', '4', '0', '0'], ['158', '01/25/2020', 'Jilin', 'Mainland China', '1/25/20 17:00', '4', '0', '0'], ['159', '01/25/2020', 'Gansu', 'Mainland China', '1/25/20 17:00', '4', '0', '0'], ['160', '01/25/2020', 'Ningxia', 'Mainland China', '1/25/20 17:00', '3', '0', '0'], ['161', '01/25/2020', 'Taiwan', 'Taiwan', '1/25/20 17:00', '3', '0', '0'], ['162', '01/25/2020', 'Xinjiang', 'Mainland China', '1/25/20 17:00', '3', '0', '0'], ['163', '01/25/2020', 'Macau', 'Macau', '1/25/20 17:00', '2', '0', '0'], ['164', '01/25/2020', 'Qinghai', 'Mainland China', '1/25/20 17:00', '1', '0', '0'], ['165', '01/25/2020', 'Washington', 'US', '1/25/20 17:00', '1', '0', '0'], ['166', '01/25/2020', 'Illinois', 'US', '1/25/20 17:00', '1', '0', '0'], ['167', '01/25/2020', '', 'Japan', '1/25/20 17:00', '2', '0', '0'], ['168', '01/25/2020', '', 'Thailand', '1/25/20 17:00', '6', '0', '3'], ['169', '01/25/2020', '', 'South Korea', '1/25/20 17:00', '2', '0', '0'], ['170', '01/25/2020', '', 'Singapore', '1/25/20 17:00', '3', '0', '0'], ['171', '01/25/2020', '', 'Vietnam', '1/25/20 17:00', '2', '0', '0'], ['172', '01/25/2020', '', 'France', '1/25/20 17:00', '3', '0', '0'], ['173', '01/25/2020', '', 'Australia', '1/25/20 17:00', '4', '0', '0'], ['174', '01/25/2020', '', 'Nepal', '1/25/20 17:00', '1', '0', '0'], ['175', '01/25/2020', '', 'Malaysia', '1/25/20 17:00', '3', '0', '0'], ['176', '01/25/2020', 'Unknown', 'China', '1/25/20 17:00', '0', '0', '0'], ['177', '01/25/2020', '', 'Kiribati', '1/25/20 17:00', '0', '0', '0'], ['178', '01/26/2020', 'Hubei', 'Mainland China', '1/26/20 16:00', '1058', '52', '42'], ['179', '01/26/2020', 'Guangdong', 'Mainland China', '1/26/20 16:00', '111', '0', '2'], ['180', '01/26/2020', 'Zhejiang', 'Mainland China', '1/26/20 16:00', '104', '0', '1'], ['181', '01/26/2020', 'Henan', 'Mainland China', '1/26/20 16:00', '83', '1', '0'], ['182', '01/26/2020', 'Chongqing', 'Mainland China', '1/26/20 16:00', '75', '0', '0'], ['183', '01/26/2020', 'Hunan', 'Mainland China', '1/26/20 16:00', '69', '0', '0'], ['184', '01/26/2020', 'Beijing', 'Mainland China', '1/26/20 16:00', '68', '0', '2'], ['185', '01/26/2020', 'Anhui', 'Mainland China', '1/26/20 16:00', '60', '0', '0'], ['186', '01/26/2020', 'Shandong', 'Mainland China', '1/26/20 16:00', '46', '0', '0'], ['187', '01/26/2020', 'Sichuan', 'Mainland China', '1/26/20 16:00', '44', '0', '0'], ['188', '01/26/2020', 'Shanghai', 'Mainland China', '1/26/20 16:00', '40', '1', '1'], ['189', '01/26/2020', 'Guangxi', 'Mainland China', '1/26/20 16:00', '36', '0', '0'], ['190', '01/26/2020', 'Jiangxi', 'Mainland China', '1/26/20 16:00', '36', '0', '0'], ['191', '01/26/2020', 'Fujian', 'Mainland China', '1/26/20 16:00', '35', '0', '0'], ['192', '01/26/2020', 'Jiangsu', 'Mainland China', '1/26/20 16:00', '33', '0', '1'], ['193', '01/26/2020', 'Hainan', 'Mainland China', '1/26/20 16:00', '22', '0', '0'], ['194', '01/26/2020', 'Shaanxi', 'Mainland China', '1/26/20 16:00', '22', '0', '0'], ['195', '01/26/2020', 'Liaoning', 'Mainland China', '1/26/20 16:00', '21', '0', '0'], ['196', '01/26/2020', 'Yunnan', 'Mainland China', '1/26/20 16:00', '16', '0', '0'], ['197', '01/26/2020', 'Heilongjiang', 'Mainland China', '1/26/20 16:00', '15', '1', '0'], ['198', '01/26/2020', 'Tianjin', 'Mainland China', '1/26/20 16:00', '14', '0', '0'], ['199', '01/26/2020', 'Hebei', 'Mainland China', '1/26/20 16:00', '13', '1', '0'], ['200', '01/26/2020', 'Shanxi', 'Mainland China', '1/26/20 16:00', '9', '0', '0'], ['201', '01/26/2020', 'Hong Kong', 'Hong Kong', '1/26/20 16:00', '8', '0', '0'], ['202', '01/26/2020', 'Inner Mongolia', 'Mainland China', '1/26/20 16:00', '7', '0', '0'], ['203', '01/26/2020', 'Gansu', 'Mainland China', '1/26/20 16:00', '7', '0', '0'], ['204', '01/26/2020', 'Guizhou', 'Mainland China', '1/26/20 16:00', '5', '0', '0'], ['205', '01/26/2020', 'Macau', 'Macau', '1/26/20 16:00', '5', '0', '0'], ['206', '01/26/2020', 'Ningxia', 'Mainland China', '1/26/20 16:00', '4', '0', '0'], ['207', '01/26/2020', 'Jilin', 'Mainland China', '1/26/20 16:00', '4', '0', '0'], ['208', '01/26/2020', 'Taiwan', 'Taiwan', '1/26/20 16:00', '4', '0', '0'], ['209', '01/26/2020', 'Xinjiang', 'Mainland China', '1/26/20 16:00', '4', '0', '0'], ['210', '01/26/2020', 'Qinghai', 'Mainland China', '1/26/20 16:00', '1', '0', '0'], ['211', '01/26/2020', 'Washington', 'US', '1/26/20 16:00', '1', '0', '0'], ['212', '01/26/2020', 'Illinois', 'US', '1/26/20 16:00', '1', '0', '0'], ['213', '01/26/2020', 'California', 'US', '1/26/20 16:00', '2', '0', '0'], ['214', '01/26/2020', 'Arizona', 'US', '1/26/20 16:00', '1', '0', '0'], ['215', '01/26/2020', '', 'Japan', '1/26/20 16:00', '4', '0', '1'], ['216', '01/26/2020', '', 'Thailand', '1/26/20 16:00', '8', '0', '6'], ['217', '01/26/2020', '', 'South Korea', '1/26/20 16:00', '3', '0', '0'], ['218', '01/26/2020', '', 'Singapore', '1/26/20 16:00', '4', '0', '0'], ['219', '01/26/2020', '', 'Vietnam', '1/26/20 16:00', '2', '0', '0'], ['220', '01/26/2020', '', 'France', '1/26/20 16:00', '3', '0', '0'], ['221', '01/26/2020', '', 'Australia', '1/26/20 16:00', '4', '0', '0'], ['222', '01/26/2020', '', 'Nepal', '1/26/20 16:00', '1', '0', '0'], ['223', '01/26/2020', '', 'Malaysia', '1/26/20 16:00', '4', '0', '0'], ['224', '01/26/2020', 'Ontario', 'Canada', '1/26/20 16:00', '1', '0', '0'], ['225', '01/26/2020', 'Unknown', 'China', '1/26/20 16:00', '0', '0', '0'], ['226', '01/26/2020', '', 'Kiribati', '1/26/20 16:00', '0', '0', '0'], ['227', '01/27/2020', 'Hubei', 'Mainland China', '1/27/20 23:59', '1423', '76', '45'], ['228', '01/27/2020', 'Guangdong', 'Mainland China', '1/27/20 23:59', '151', '0', '4'], ['229', '01/27/2020', 'Zhejiang', 'Mainland China', '1/27/20 23:59', '128', '0', '1'], ['230', '01/27/2020', 'Henan', 'Mainland China', '1/27/20 23:59', '128', '1', '0'], ['231', '01/27/2020', 'Chongqing', 'Mainland China', '1/27/20 23:59', '110', '0', '0'], ['232', '01/27/2020', 'Hunan', 'Mainland China', '1/27/20 23:59', '100', '0', '0'], ['233', '01/27/2020', 'Beijing', 'Mainland China', '1/27/20 23:59', '80', '1', '2'], ['234', '01/27/2020', 'Shandong', 'Mainland China', '1/27/20 23:59', '75', '0', '0'], ['235', '01/27/2020', 'Jiangxi', 'Mainland China', '1/27/20 23:59', '72', '0', '2'], ['236', '01/27/2020', 'Anhui', 'Mainland China', '1/27/20 23:59', '70', '0', '0'], ['237', '01/27/2020', 'Sichuan', 'Mainland China', '1/27/20 23:59', '69', '0', '0'], ['238', '01/27/2020', 'Fujian', 'Mainland China', '1/27/20 23:59', '59', '0', '0'], ['239', '01/27/2020', 'Shanghai', 'Mainland China', '1/27/20 23:59', '53', '1', '3'], ['240', '01/27/2020', 'Jiangsu', 'Mainland China', '1/27/20 23:59', '47', '0', '1'], ['241', '01/27/2020', 'Guangxi', 'Mainland China', '1/27/20 23:59', '46', '0', '0'], ['242', '01/27/2020', 'Shaanxi', 'Mainland China', '1/27/20 23:59', '35', '0', '0'], ['243', '01/27/2020', 'Hainan', 'Mainland China', '1/27/20 23:59', '33', '1', '0'], ['244', '01/27/2020', 'Liaoning', 'Mainland China', '1/27/20 23:59', '27', '0', '0'], ['245', '01/27/2020', 'Yunnan', 'Mainland China', '1/27/20 23:59', '26', '0', '0'], ['246', '01/27/2020', 'Tianjin', 'Mainland China', '1/27/20 23:59', '23', '0', '0'], ['247', '01/27/2020', 'Heilongjiang', 'Mainland China', '1/27/20 23:59', '21', '1', '0'], ['248', '01/27/2020', 'Hebei', 'Mainland China', '1/27/20 23:59', '18', '1', '0'], ['249', '01/27/2020', 'Gansu', 'Mainland China', '1/27/20 23:59', '14', '0', '0'], ['250', '01/27/2020', 'Shanxi', 'Mainland China', '1/27/20 23:59', '13', '0', '0'], ['251', '01/27/2020', 'Inner Mongolia', 'Mainland China', '1/27/20 23:59', '11', '0', '0'], ['252', '01/27/2020', 'Hong Kong', 'Hong Kong', '1/27/20 23:59', '8', '0', '0'], ['253', '01/27/2020', 'Guizhou', 'Mainland China', '1/27/20 23:59', '7', '0', '0'], ['254', '01/27/2020', 'Ningxia', 'Mainland China', '1/27/20 23:59', '7', '0', '0'], ['255', '01/27/2020', 'Jilin', 'Mainland China', '1/27/20 23:59', '6', '0', '0'], ['256', '01/27/2020', 'Macau', 'Macau', '1/27/20 23:59', '6', '0', '0'], ['257', '01/27/2020', 'Qinghai', 'Mainland China', '1/27/20 23:59', '6', '0', '0'], ['258', '01/27/2020', 'Taiwan', 'Taiwan', '1/27/20 23:59', '5', '0', '0'], ['259', '01/27/2020', 'Xinjiang', 'Mainland China', '1/27/20 23:59', '5', '0', '0'], ['260', '01/27/2020', 'Washington', 'US', '1/27/20 23:59', '1', '0', '0'], ['261', '01/27/2020', 'Illinois', 'US', '1/27/20 23:59', '1', '0', '0'], ['262', '01/27/2020', 'California', 'US', '1/27/20 23:59', '2', '0', '0'], ['263', '01/27/2020', 'Arizona', 'US', '1/27/20 23:59', '1', '0', '0'], ['264', '01/27/2020', '', 'Japan', '1/27/20 23:59', '4', '0', '1'], ['265', '01/27/2020', '', 'Thailand', '1/27/20 23:59', '8', '0', '6'], ['266', '01/27/2020', '', 'South Korea', '1/27/20 23:59', '4', '0', '0'], ['267', '01/27/2020', '', 'Singapore', '1/27/20 23:59', '5', '0', '0'], ['268', '01/27/2020', '', 'Vietnam', '1/27/20 23:59', '2', '0', '0'], ['269', '01/27/2020', '', 'France', '1/27/20 23:59', '3', '0', '0'], ['270', '01/27/2020', '', 'Nepal', '1/27/20 23:59', '1', '0', '0'], ['271', '01/27/2020', '', 'Malaysia', '1/27/20 23:59', '4', '0', '0'], ['272', '01/27/2020', 'Ontario', 'Canada', '1/27/20 23:59', '1', '0', '0'], ['273', '01/27/2020', '', 'Cambodia', '1/27/20 23:59', '1', '0', '0'], ['274', '01/27/2020', '', 'Sri Lanka', '1/27/20 23:59', '1', '0', '0'], ['275', '01/27/2020', '', 'Ivory Coast', '1/27/20 23:59', '1', '0', '0'], ['276', '01/27/2020', 'New South Wales', 'Australia', '1/27/20 23:59', '4', '0', '0'], ['277', '01/27/2020', 'Victoria', 'Australia', '1/27/20 23:59', '1', '0', '0'], ['278', '01/27/2020', 'Unknown', 'China', '1/27/20 23:59', '0', '0', '0'], ['279', '01/27/2020', '', 'Kiribati', '1/27/20 23:59', '0', '0', '0'], ['280', '01/28/2020', 'Hubei', 'Mainland China', '1/28/20 23:00', '3554', '125', '80'], ['281', '01/28/2020', 'Guangdong', 'Mainland China', '1/28/20 23:00', '207', '0', '4'], ['282', '01/28/2020', 'Zhejiang', 'Mainland China', '1/28/20 23:00', '173', '0', '3'], ['283', '01/28/2020', 'Henan', 'Mainland China', '1/28/20 23:00', '168', '1', '0'], ['284', '01/28/2020', 'Hunan', 'Mainland China', '1/28/20 23:00', '143', '0', '0'], ['285', '01/28/2020', 'Chongqing', 'Mainland China', '1/28/20 23:00', '132', '0', '0'], ['286', '01/28/2020', 'Jiangxi', 'Mainland China', '1/28/20 23:00', '109', '0', '3'], ['287', '01/28/2020', 'Anhui', 'Mainland China', '1/28/20 23:00', '106', '0', '0'], ['288', '01/28/2020', 'Shandong', 'Mainland China', '1/28/20 23:00', '95', '0', '0'], ['289', '01/28/2020', 'Beijing', 'Mainland China', '1/28/20 23:00', '91', '1', '4'], ['290', '01/28/2020', 'Sichuan', 'Mainland China', '1/28/20 23:00', '90', '0', '0'], ['291', '01/28/2020', 'Fujian', 'Mainland China', '1/28/20 23:00', '80', '0', '0'], ['292', '01/28/2020', 'Jiangsu', 'Mainland China', '1/28/20 23:00', '70', '0', '1'], ['293', '01/28/2020', 'Shanghai', 'Mainland China', '1/28/20 23:00', '66', '1', '4'], ['294', '01/28/2020', 'Guangxi', 'Mainland China', '1/28/20 23:00', '51', '0', '2'], ['295', '01/28/2020', 'Shaanxi', 'Mainland China', '1/28/20 23:00', '46', '0', '0'], ['296', '01/28/2020', 'Yunnan', 'Mainland China', '1/28/20 23:00', '44', '0', '0'], ['297', '01/28/2020', 'Hainan', 'Mainland China', '1/28/20 23:00', '40', '1', '0'], ['298', '01/28/2020', 'Liaoning', 'Mainland China', '1/28/20 23:00', '34', '0', '0'], ['299', '01/28/2020', 'Hebei', 'Mainland China', '1/28/20 23:00', '33', '1', '0'], ['300', '01/28/2020', 'Heilongjiang', 'Mainland China', '1/28/20 23:00', '33', '1', '0'], ['301', '01/28/2020', 'Shanxi', 'Mainland China', '1/28/20 23:00', '27', '0', '0'], ['302', '01/28/2020', 'Tianjin', 'Mainland China', '1/28/20 23:00', '24', '0', '0'], ['303', '01/28/2020', 'Gansu', 'Mainland China', '1/28/20 23:00', '19', '0', '0'], ['304', '01/28/2020', 'Inner Mongolia', 'Mainland China', '1/28/20 23:00', '15', '0', '0'], ['305', '01/28/2020', 'Ningxia', 'Mainland China', '1/28/20 23:00', '11', '0', '0'], ['306', '01/28/2020', 'Xinjiang', 'Mainland China', '1/28/20 23:00', '10', '0', '0'], ['307', '01/28/2020', 'Guizhou', 'Mainland China', '1/28/20 23:00', '9', '0', '0'], ['308', '01/28/2020', 'Jilin', 'Mainland China', '1/28/20 23:00', '8', '0', '0'], ['309', '01/28/2020', 'Taiwan', 'Taiwan', '1/28/20 23:00', '8', '0', '0'], ['310', '01/28/2020', 'Hong Kong', 'Hong Kong', '1/28/20 23:00', '8', '0', '0'], ['311', '01/28/2020', 'Macau', 'Macau', '1/28/20 23:00', '7', '0', '0'], ['312', '01/28/2020', 'Qinghai', 'Mainland China', '1/28/20 23:00', '6', '0', '0'], ['313', '01/28/2020', 'Washington', 'US', '1/28/20 23:00', '1', '0', '0'], ['314', '01/28/2020', 'Illinois', 'US', '1/28/20 23:00', '1', '0', '0'], ['315', '01/28/2020', 'California', 'US', '1/28/20 23:00', '2', '0', '0'], ['316', '01/28/2020', 'Arizona', 'US', '1/28/20 23:00', '1', '0', '0'], ['317', '01/28/2020', '', 'Japan', '1/28/20 23:00', '7', '0', '1'], ['318', '01/28/2020', '', 'Thailand', '1/28/20 23:00', '14', '0', '6'], ['319', '01/28/2020', '', 'South Korea', '1/28/20 23:00', '4', '0', '0'], ['320', '01/28/2020', '', 'Singapore', '1/28/20 23:00', '7', '0', '0'], ['321', '01/28/2020', '', 'Vietnam', '1/28/20 23:00', '2', '0', '0'], ['322', '01/28/2020', '', 'France', '1/28/20 23:00', '4', '0', '0'], ['323', '01/28/2020', '', 'Nepal', '1/28/20 23:00', '1', '0', '0'], ['324', '01/28/2020', '', 'Malaysia', '1/28/20 23:00', '4', '0', '0'], ['325', '01/28/2020', 'Ontario', 'Canada', '1/28/20 23:00', '1', '0', '0'], ['326', '01/28/2020', 'British Columbia', 'Canada', '1/28/20 23:00', '1', '0', '0'], ['327', '01/28/2020', '', 'Cambodia', '1/28/20 23:00', '1', '0', '0'], ['328', '01/28/2020', '', 'Sri Lanka', '1/28/20 23:00', '1', '0', '0'], ['329', '01/28/2020', 'New South Wales', 'Australia', '1/28/20 23:00', '4', '0', '0'], ['330', '01/28/2020', 'Victoria', 'Australia', '1/28/20 23:00', '1', '0', '0'], ['331', '01/28/2020', 'Bavaria', 'Germany', '1/28/20 23:00', '4', '0', '0'], ['332', '01/28/2020', 'Unknown', 'China', '1/28/20 23:00', '0', '0', '0'], ['333', '01/28/2020', '', 'Kiribati', '1/28/20 23:00', '0', '0', '0'], ['334', '01/29/2020', 'Hubei', 'Mainland China', '1/29/20 19:30', '3554', '125', '88'], ['335', '01/29/2020', 'Zhejiang', 'Mainland China', '1/29/20 19:30', '296', '0', '3'], ['336', '01/29/2020', 'Guangdong', 'Mainland China', '1/29/20 19:30', '277', '0', '5'], ['337', '01/29/2020', 'Hunan', 'Mainland China', '1/29/20 19:30', '221', '0', '0'], ['338', '01/29/2020', 'Henan', 'Mainland China', '1/29/20 19:30', '206', '2', '1'], ['339', '01/29/2020', 'Anhui', 'Mainland China', '1/29/20 19:30', '152', '0', '2'], ['340', '01/29/2020', 'Chongqing', 'Mainland China', '1/29/20 19:30', '147', '0', '1'], ['341', '01/29/2020', 'Shandong', 'Mainland China', '1/29/20 19:30', '130', '0', '1'], ['342', '01/29/2020', 'Beijing', 'Mainland China', '1/29/20 19:30', '111', '1', '4'], ['343', '01/29/2020', 'Jiangxi', 'Mainland China', '1/29/20 19:30', '109', '0', '3'], ['344', '01/29/2020', 'Sichuan', 'Mainland China', '1/29/20 19:30', '108', '1', '1'], ['345', '01/29/2020', 'Jiangsu', 'Mainland China', '1/29/20 19:30', '99', '0', '1'], ['346', '01/29/2020', 'Shanghai', 'Mainland China', '1/29/20 19:30', '96', '1', '5'], ['347', '01/29/2020', 'Fujian', 'Mainland China', '1/29/20 19:30', '84', '0', '0'], ['348', '01/29/2020', 'Guangxi', 'Mainland China', '1/29/20 19:30', '58', '0', '2'], ['349', '01/29/2020', 'Shaanxi', 'Mainland China', '1/29/20 19:30', '56', '0', '0'], ['350', '01/29/2020', 'Yunnan', 'Mainland China', '1/29/20 19:30', '55', '0', '0'], ['351', '01/29/2020', 'Hebei', 'Mainland China', '1/29/20 19:30', '48', '1', '0'], ['352', '01/29/2020', 'Hainan', 'Mainland China', '1/29/20 19:30', '43', '1', '0'], ['353', '01/29/2020', 'Liaoning', 'Mainland China', '1/29/20 19:30', '39', '0', '1'], ['354', '01/29/2020', 'Heilongjiang', 'Mainland China', '1/29/20 19:30', '38', '1', '0'], ['355', '01/29/2020', 'Tianjin', 'Mainland China', '1/29/20 19:30', '27', '0', '0'], ['356', '01/29/2020', 'Shanxi', 'Mainland China', '1/29/20 19:30', '27', '0', '1'], ['357', '01/29/2020', 'Gansu', 'Mainland China', '1/29/20 19:30', '24', '0', '0'], ['358', '01/29/2020', 'Inner Mongolia', 'Mainland China', '1/29/20 19:30', '16', '0', '0'], ['359', '01/29/2020', 'Xinjiang', 'Mainland China', '1/29/20 19:30', '13', '0', '0'], ['360', '01/29/2020', 'Ningxia', 'Mainland China', '1/29/20 19:30', '12', '0', '0'], ['361', '01/29/2020', 'Hong Kong', 'Hong Kong', '1/29/20 19:30', '10', '0', '0'], ['362', '01/29/2020', 'Guizhou', 'Mainland China', '1/29/20 19:30', '9', '0', '1'], ['363', '01/29/2020', 'Jilin', 'Mainland China', '1/29/20 19:30', '9', '0', '0'], ['364', '01/29/2020', 'Taiwan', 'Taiwan', '1/29/20 19:30', '8', '0', '0'], ['365', '01/29/2020', 'Macau', 'Macau', '1/29/20 19:30', '7', '0', '0'], ['366', '01/29/2020', 'Qinghai', 'Mainland China', '1/29/20 19:30', '6', '0', '0'], ['367', '01/29/2020', 'Washington', 'US', '1/29/20 19:30', '1', '0', '0'], ['368', '01/29/2020', 'Illinois', 'US', '1/29/20 19:30', '1', '0', '0'], ['369', '01/29/2020', 'California', 'US', '1/29/20 19:30', '2', '0', '0'], ['370', '01/29/2020', 'Arizona', 'US', '1/29/20 19:30', '1', '0', '0'], ['371', '01/29/2020', '', 'Japan', '1/29/20 19:30', '7', '0', '1'], ['372', '01/29/2020', '', 'Thailand', '1/29/20 19:30', '14', '0', '6'], ['373', '01/29/2020', '', 'South Korea', '1/29/20 19:30', '4', '0', '0'], ['374', '01/29/2020', '', 'Singapore', '1/29/20 19:30', '7', '0', '0'], ['375', '01/29/2020', '', 'Vietnam', '1/29/20 19:30', '2', '0', '0'], ['376', '01/29/2020', '', 'France', '1/29/20 19:30', '5', '0', '0'], ['377', '01/29/2020', '', 'Nepal', '1/29/20 19:30', '1', '0', '0'], ['378', '01/29/2020', '', 'Malaysia', '1/29/20 19:30', '7', '0', '0'], ['379', '01/29/2020', 'Ontario', 'Canada', '1/29/20 19:30', '1', '0', '0'], ['380', '01/29/2020', 'British Columbia', 'Canada', '1/29/20 19:30', '1', '0', '0'], ['381', '01/29/2020', '', 'Cambodia', '1/29/20 19:30', '1', '0', '0'], ['382', '01/29/2020', '', 'Sri Lanka', '1/29/20 19:30', '1', '0', '0'], ['383', '01/29/2020', 'New South Wales', 'Australia', '1/29/20 19:30', '4', '0', '0'], ['384', '01/29/2020', 'Victoria', 'Australia', '1/29/20 19:30', '1', '0', '0'], ['385', '01/29/2020', 'Bavaria', 'Germany', '1/29/20 19:30', '4', '0', '0'], ['386', '01/29/2020', '', 'Finland', '1/29/20 19:30', '1', '0', '0'], ['387', '01/29/2020', '', 'United Arab Emirates', '1/29/20 19:30', '4', '0', '0'], ['388', '01/29/2020', 'Unknown', 'China', '1/29/20 19:30', '0', '0', '0'], ['389', '01/29/2020', '', 'Kiribati', '1/29/20 19:30', '0', '0', '0'], ['390', '01/30/2020', 'Hubei', 'Mainland China', '1/30/20 16:00', '4903', '162', '90'], ['391', '01/30/2020', 'Zhejiang', 'Mainland China', '1/30/20 16:00', '428', '0', '4'], ['392', '01/30/2020', 'Guangdong', 'Mainland China', '1/30/20 16:00', '354', '0', '10'], ['393', '01/30/2020', 'Henan', 'Mainland China', '1/30/20 16:00', '278', '2', '2'], ['394', '01/30/2020', 'Hunan', 'Mainland China', '1/30/20 16:00', '277', '0', '2'], ['395', '01/30/2020', 'Anhui', 'Mainland China', '1/30/20 16:00', '200', '0', '2'], ['396', '01/30/2020', 'Chongqing', 'Mainland China', '1/30/20 16:00', '182', '0', '1'], ['397', '01/30/2020', 'Jiangxi', 'Mainland China', '1/30/20 16:00', '162', '0', '5'], ['398', '01/30/2020', 'Shandong', 'Mainland China', '1/30/20 16:00', '158', '0', '1'], ['399', '01/30/2020', 'Sichuan', 'Mainland China', '1/30/20 16:00', '142', '1', '1'], ['400', '01/30/2020', 'Jiangsu', 'Mainland China', '1/30/20 16:00', '129', '0', '1'], ['401', '01/30/2020', 'Beijing', 'Mainland China', '1/30/20 16:00', '114', '1', '4'], ['402', '01/30/2020', 'Shanghai', 'Mainland China', '1/30/20 16:00', '112', '1', '5'], ['403', '01/30/2020', 'Fujian', 'Mainland China', '1/30/20 16:00', '101', '0', '0'], ['404', '01/30/2020', 'Guangxi', 'Mainland China', '1/30/20 16:00', '78', '0', '2'], ['405', '01/30/2020', 'Yunnan', 'Mainland China', '1/30/20 16:00', '70', '0', '0'], ['406', '01/30/2020', 'Hebei', 'Mainland China', '1/30/20 16:00', '65', '1', '0'], ['407', '01/30/2020', 'Shaanxi', 'Mainland China', '1/30/20 16:00', '63', '0', '0'], ['408', '01/30/2020', 'Hainan', 'Mainland China', '1/30/20 16:00', '46', '1', '1'], ['409', '01/30/2020', 'Heilongjiang', 'Mainland China', '1/30/20 16:00', '44', '2', '0'], ['410', '01/30/2020', 'Liaoning', 'Mainland China', '1/30/20 16:00', '41', '0', '1'], ['411', '01/30/2020', 'Shanxi', 'Mainland China', '1/30/20 16:00', '35', '0', '1'], ['412', '01/30/2020', 'Tianjin', 'Mainland China', '1/30/20 16:00', '31', '0', '0'], ['413', '01/30/2020', 'Gansu', 'Mainland China', '1/30/20 16:00', '26', '0', '0'], ['414', '01/30/2020', 'Inner Mongolia', 'Mainland China', '1/30/20 16:00', '19', '0', '0'], ['415', '01/30/2020', 'Ningxia', 'Mainland China', '1/30/20 16:00', '17', '0', '0'], ['416', '01/30/2020', 'Jilin', 'Mainland China', '1/30/20 16:00', '14', '0', '1'], ['417', '01/30/2020', 'Xinjiang', 'Mainland China', '1/30/20 16:00', '14', '0', '0'], ['418', '01/30/2020', 'Guizhou', 'Mainland China', '1/30/20 16:00', '12', '0', '1'], ['419', '01/30/2020', 'Hong Kong', 'Hong Kong', '1/30/20 16:00', '10', '0', '0'], ['420', '01/30/2020', 'Taiwan', 'Taiwan', '1/30/20 16:00', '9', '0', '0'], ['421', '01/30/2020', 'Qinghai', 'Mainland China', '1/30/20 16:00', '8', '0', '0'], ['422', '01/30/2020', 'Macau', 'Macau', '1/30/20 16:00', '7', '0', '0'], ['423', '01/30/2020', 'Tibet', 'Mainland China', '1/30/20 16:00', '1', '0', '0'], ['424', '01/30/2020', 'Washington', 'US', '1/30/20 16:00', '1', '0', '0'], ['425', '01/30/2020', 'Illinois', 'US', '1/30/20 16:00', '1', '0', '0'], ['426', '01/30/2020', 'California', 'US', '1/30/20 16:00', '2', '0', '0'], ['427', '01/30/2020', 'Arizona', 'US', '1/30/20 16:00', '1', '0', '0'], ['428', '01/30/2020', '', 'Japan', '1/30/20 16:00', '11', '0', '1'], ['429', '01/30/2020', '', 'Thailand', '1/30/20 16:00', '14', '0', '7'], ['430', '01/30/2020', '', 'South Korea', '1/30/20 16:00', '4', '0', '0'], ['431', '01/30/2020', '', 'Singapore', '1/30/20 16:00', '10', '0', '0'], ['432', '01/30/2020', '', 'Vietnam', '1/30/20 16:00', '2', '0', '0'], ['433', '01/30/2020', '', 'France', '1/30/20 16:00', '5', '0', '0'], ['434', '01/30/2020', '', 'Nepal', '1/30/20 16:00', '1', '0', '0'], ['435', '01/30/2020', '', 'Malaysia', '1/30/20 16:00', '8', '0', '0'], ['436', '01/30/2020', 'Ontario', 'Canada', '1/30/20 16:00', '2', '0', '0'], ['437', '01/30/2020', 'British Columbia', 'Canada', '1/30/20 16:00', '1', '0', '0'], ['438', '01/30/2020', '', 'Cambodia', '1/30/20 16:00', '1', '0', '0'], ['439', '01/30/2020', '', 'Sri Lanka', '1/30/20 16:00', '1', '0', '0'], ['440', '01/30/2020', 'New South Wales', 'Australia', '1/30/20 16:00', '4', '0', '2'], ['441', '01/30/2020', 'Victoria', 'Australia', '1/30/20 16:00', '2', '0', '0'], ['442', '01/30/2020', 'Queensland', 'Australia', '1/30/20 16:00', '3', '0', '0'], ['443', '01/30/2020', 'Bavaria', 'Germany', '1/30/20 16:00', '4', '0', '0'], ['444', '01/30/2020', '', 'Finland', '1/30/20 16:00', '1', '0', '0'], ['445', '01/30/2020', '', 'United Arab Emirates', '1/30/20 16:00', '4', '0', '0'], ['446', '01/30/2020', '', 'Philippines', '1/30/20 16:00', '1', '0', '0'], ['447', '01/30/2020', '', 'India', '1/30/20 16:00', '1', '0', '0'], ['448', '01/30/2020', 'Unknown', 'China', '1/30/20 16:00', '0', '0', '0'], ['449', '01/30/2020', '', 'Kiribati', '1/30/20 16:00', '0', '0', '0'], ['450', '01/31/2020', 'Hubei', 'Mainland China', '1/31/2020 23:59', '5806', '204', '141'], ['451', '01/31/2020', 'Zhejiang', 'Mainland China', '1/31/2020 23:59', '538', '0', '14'], ['452', '01/31/2020', 'Guangdong', 'Mainland China', '1/31/2020 23:59', '436', '0', '11'], ['453', '01/31/2020', 'Henan', 'Mainland China', '1/31/2020 23:59', '352', '2', '3'], ['454', '01/31/2020', 'Hunan', 'Mainland China', '1/31/2020 23:59', '332', '0', '2'], ['455', '01/31/2020', 'Jiangxi', 'Mainland China', '1/31/2020 23:59', '240', '0', '7'], ['456', '01/31/2020', 'Anhui', 'Mainland China', '1/31/2020 23:59', '237', '0', '3'], ['457', '01/31/2020', 'Chongqing', 'Mainland China', '1/31/2020 23:59', '211', '0', '1'], ['458', '01/31/2020', 'Shandong', 'Mainland China', '1/31/2020 23:59', '184', '0', '2'], ['459', '01/31/2020', 'Sichuan', 'Mainland China', '1/31/2020 23:59', '177', '1', '1'], ['460', '01/31/2020', 'Jiangsu', 'Mainland China', '1/31/2020 23:59', '168', '0', '5'], ['461', '01/31/2020', 'Beijing', 'Mainland China', '1/31/2020 23:59', '139', '1', '5'], ['462', '01/31/2020', 'Shanghai', 'Mainland China', '1/31/2020 23:59', '135', '1', '9'], ['463', '01/31/2020', 'Fujian', 'Mainland China', '1/31/2020 23:59', '120', '0', '0'], ['464', '01/31/2020', 'Guangxi', 'Mainland China', '1/31/2020 23:59', '87', '0', '2'], ['465', '01/31/2020', 'Shaanxi', 'Mainland China', '1/31/2020 23:59', '87', '0', '0'], ['466', '01/31/2020', 'Yunnan', 'Mainland China', '1/31/2020 23:59', '83', '0', '1'], ['467', '01/31/2020', 'Hebei', 'Mainland China', '1/31/2020 23:59', '82', '1', '0'], ['468', '01/31/2020', 'Heilongjiang', 'Mainland China', '1/31/2020 23:59', '59', '2', '0'], ['469', '01/31/2020', 'Hainan', 'Mainland China', '1/31/2020 23:59', '52', '1', '1'], ['470', '01/31/2020', 'Liaoning', 'Mainland China', '1/31/2020 23:59', '48', '0', '1'], ['471', '01/31/2020', 'Shanxi', 'Mainland China', '1/31/2020 23:59', '39', '0', '1'], ['472', '01/31/2020', 'Tianjin', 'Mainland China', '1/31/2020 23:59', '32', '0', '0'], ['473', '01/31/2020', 'Guizhou', 'Mainland China', '1/31/2020 23:59', '29', '0', '2'], ['474', '01/31/2020', 'Gansu', 'Mainland China', '1/31/2020 23:59', '29', '0', '0'], ['475', '01/31/2020', 'Ningxia', 'Mainland China', '1/31/2020 23:59', '21', '0', '0'], ['476', '01/31/2020', 'Inner Mongolia', 'Mainland China', '1/31/2020 23:59', '20', '0', '1'], ['477', '01/31/2020', 'Xinjiang', 'Mainland China', '1/31/2020 23:59', '17', '0', '0'], ['478', '01/31/2020', 'Jilin', 'Mainland China', '1/31/2020 23:59', '14', '0', '1'], ['479', '01/31/2020', 'Hong Kong', 'Hong Kong', '1/31/2020 23:59', '12', '0', '0'], ['480', '01/31/2020', 'Taiwan', 'Taiwan', '1/31/2020 23:59', '10', '0', '0'], ['481', '01/31/2020', 'Qinghai', 'Mainland China', '1/31/2020 23:59', '8', '0', '0'], ['482', '01/31/2020', 'Macau', 'Macau', '1/31/2020 23:59', '7', '0', '0'], ['483', '01/31/2020', 'Tibet', 'Mainland China', '1/31/2020 23:59', '1', '0', '0'], ['484', '01/31/2020', '', 'Thailand', '1/31/2020 23:59', '19', '0', '8'], ['485', '01/31/2020', '', 'Japan', '1/31/2020 23:59', '15', '0', '1'], ['486', '01/31/2020', '', 'Singapore', '1/31/2020 23:59', '13', '0', '0'], ['487', '01/31/2020', '', 'South Korea', '1/31/2020 23:59', '11', '0', '0'], ['488', '01/31/2020', '', 'Malaysia', '1/31/2020 23:59', '8', '0', '0'], ['489', '01/31/2020', '', 'France', '1/31/2020 23:59', '5', '0', '0'], ['490', '01/31/2020', 'Bavaria', 'Germany', '1/31/2020 23:59', '5', '0', '0'], ['491', '01/31/2020', 'New South Wales', 'Australia', '1/31/2020 23:59', '4', '0', '2'], ['492', '01/31/2020', '', 'United Arab Emirates', '1/31/2020 23:59', '4', '0', '0'], ['493', '01/31/2020', 'Victoria', 'Australia', '1/31/2020 23:59', '3', '0', '0'], ['494', '01/31/2020', 'Illinois', 'US', '1/31/2020 23:59', '2', '0', '0'], ['495', '01/31/2020', 'California', 'US', '1/31/2020 23:59', '2', '0', '0'], ['496', '01/31/2020', '', 'Vietnam', '1/31/2020 23:59', '2', '0', '0'], ['497', '01/31/2020', 'Ontario', 'Canada', '1/31/2020 23:59', '2', '0', '0'], ['498', '01/31/2020', 'Queensland', 'Australia', '1/31/2020 23:59', '2', '0', '0'], ['499', '01/31/2020', '', 'Italy', '1/31/2020 23:59', '2', '0', '0'], ['500', '01/31/2020', '', 'UK', '1/31/2020 23:59', '2', '0', '0'], ['501', '01/31/2020', '', 'Russia', '1/31/2020 23:59', '2', '0', '0'], ['502', '01/31/2020', 'Washington', 'US', '1/31/2020 23:59', '1', '0', '0'], ['503', '01/31/2020', 'Arizona', 'US', '1/31/2020 23:59', '1', '0', '0'], ['504', '01/31/2020', '', 'Nepal', '1/31/2020 23:59', '1', '0', '0'], ['505', '01/31/2020', 'British Columbia', 'Canada', '1/31/2020 23:59', '1', '0', '0'], ['506', '01/31/2020', '', 'Cambodia', '1/31/2020 23:59', '1', '0', '0'], ['507', '01/31/2020', '', 'Sri Lanka', '1/31/2020 23:59', '1', '0', '0'], ['508', '01/31/2020', '', 'Finland', '1/31/2020 23:59', '1', '0', '0'], ['509', '01/31/2020', '', 'Philippines', '1/31/2020 23:59', '1', '0', '0'], ['510', '01/31/2020', '', 'India', '1/31/2020 23:59', '1', '0', '0'], ['511', '01/31/2020', '', 'Sweden', '1/31/2020 23:59', '1', '0', '0'], ['512', '01/31/2020', 'Unknown', 'China', '1/31/2020 23:59', '0', '0', '0'], ['513', '01/31/2020', '', 'Kiribati', '1/31/2020 23:59', '0', '0', '0']])

"""
def drop_tables():
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    sql_query = "DROP TABLE countries_regions"
    cursor.execute(sql_query)
    db.commit()
    sql_query = "DROP TABLE provinces_states"
    cursor.execute(sql_query)
    db.commit()
    sql_query = "DROP TABLE dates"
    cursor.execute(sql_query)
    db.commit()
    sql_query = "DROP TABLE records"
    cursor.execute(sql_query)
    db.commit()
    sql_query = "DROP TABLE statistics"
    cursor.execute(sql_query)
    db.commit()
    db.close()
drop_tables()
#"""

# ================================================

#TASK 23: Retrieve the names of all (unique) countries in alphabetical order
def unique_countries_alphabetical_order():
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    sql_query = "SELECT DISTINCT countries_regions.country_region FROM countries_regions ORDER BY countries_regions.country_region ASC;"
    cursor.execute(sql_query)
    all_records = cursor.fetchall()
    #print("Retrieved the names of all (unique) countries in alphabetical order: ")
    outcome = []
    for rec in all_records:
        outcome.append(rec[0])
    db.close()
    return outcome

#print(unique_countries_alphabetical_order())


#ADDITIONAL FUNCTION: Check if a sno is in the db //// for Task 24
def check_if_a_sno_is_in_db(sno):
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    serial_no = [sno]
    sql_query = "SELECT records.sno FROM records WHERE records.sno = ?"
    cursor.execute(sql_query, serial_no)
    all_records = cursor.fetchall()
    #print(all_records)
    db.close()
    if all_records == []:
        return False
    else:
        return True


#print(check_if_a_sno_is_in_db(513))
#print(check_if_a_sno_is_in_db(555))


#TASK 24: Retrieve the number of confirmed cases, deaths and recoveries for a specified observation(record) / serial number.
def number_confirmed_deaths_recovered_by_sno():
    stop = 0
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    while stop == 0:
        s_no = tui.serial_number()
        if check_if_a_sno_is_in_db(s_no) == False:
            tui.error("No such serial number in the database, please try again below")
        else:
            stop = 1
            serial_no = [s_no]
            sql_query = "SELECT statistics.confirmed, statistics.deaths, statistics.recovered FROM statistics INNER JOIN records ON statistics.record_id = records.record_id WHERE records.sno = ?"
            cursor.execute(sql_query, serial_no)
            all_records = cursor.fetchall()
            #print(all_records)
            for rec in all_records:
                c = rec[0]
                d = rec[1]
                r = rec[2]
            outcome = []
            outcome.append(s_no)
            outcome.append(c)
            outcome.append(d)
            outcome.append(r)
            return outcome
    db.close()

#print(number_confirmed_deaths_recovered_by_sno())


#TASK 25: Retrieve information for the top 5 countries for confirmed cases
def retrieve_info_top5_countries_confirmed_cases():
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    sql_query = "SELECT statistics.confirmed, countries_regions.country_region, SUM(statistics.confirmed) as sum_confirmed FROM countries_regions INNER JOIN records ON countries_regions.country_region_id = records.country_region_id INNER JOIN statistics ON records.record_id=statistics.record_id GROUP BY countries_regions.country_region ORDER BY sum_confirmed DESC"
    cursor.execute(sql_query, )
    all_records = cursor.fetchall()
    #print(all_records)
    stop = 0
    outcome = []
    #final_outcome=[]
    for rec in all_records:
        stop = stop+1
        #outcome.append(f"{rec[1]}: {rec[2]}")
        outcome.append(rec[1])
        outcome.append(rec[2])
        if stop == 5:
            break
    db.close()
    return outcome

#print(retrieve_info_top5_countries_confirmed_cases())


#TASK 26: Retrieve information for the top 5 countries for death for specific observation dates
def retrieve_info_top5_countries_deaths_obsdate():
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    obs_dates = tui.observation_dates()
    final_outcome = []
    for od in obs_dates:
        value = [od]
        sql_query = "SELECT statistics.deaths, countries_regions.country_region, SUM(statistics.deaths) as sum_deaths FROM countries_regions INNER JOIN records ON countries_regions.country_region_id = records.country_region_id INNER JOIN statistics ON records.record_id=statistics.record_id INNER JOIN dates ON records.dates_id=dates.dates_id WHERE dates.observation_date = ? GROUP BY countries_regions.country_region ORDER BY sum_deaths DESC"
        cursor.execute(sql_query, value)
        all_records = cursor.fetchall()
        #print(all_records)
        stop = 0
        outcome = []
        outcome.append(f"Observation date: {od}")
        for rec in all_records:
            stop = stop + 1
            outcome.append(rec[1])
            outcome.append(rec[2])
            #outcome.append(f"{rec[1]}: {rec[2]}")
            if stop == 5:
                break
        final_outcome.append(outcome)
    db.close()
    return final_outcome
    
#print(retrieve_info_top5_countries_deaths_obsdate())


#Additional function: Check if a country is inside the db [3]->[3] Animated Summary //// for Task 30
def check_if_a_country_is_in_db(country_name):
    unique_countries = unique_countries_alphabetical_order()
    found = 0
    for con in unique_countries:
        if country_name == con:
            found = 1
    if found == 0:
        return False
    else:
        return True

#print(check_if_a_country_is_in_db())


#Additional function: Made for visualisation exercise [3]->[3] Animated Summary //// for Task 30
def number_confirmed_deaths_recovered_by_obsdate_country():
    db = sqlite3.connect("covid_db.db")
    cursor = db.cursor()
    stop = 0
    stop2 = 0
    stop3 = 0
    while stop == 0:
        country = tui.get_a_country_for_visualisation()
        c = 0
        d = 0
        r = 0
        if check_if_a_country_is_in_db(country) == False:
            tui.error("No such country in the database, please try again below")
        else:
            stop = 1
            country_value = [country]
            sql_query = "SELECT SUM(statistics.confirmed) as sum_confirmed, SUM(statistics.deaths) as sum_deaths, SUM(statistics.recovered) as sum_recovered, dates.observation_date, countries_regions.country_region FROM dates INNER JOIN records ON dates.dates_id = records.dates_id INNER JOIN countries_regions ON records.country_region_id=countries_regions.country_region_id INNER JOIN statistics ON records.record_id=statistics.record_id WHERE countries_regions.country_region=? GROUP BY countries_regions.country_region, dates.observation_date ORDER BY dates.observation_date ASC"
            cursor.execute(sql_query, country_value)
            all_records = cursor.fetchall()
            final_list = []
            final_list.append(all_records)
            while stop2 == 0:
                choice = input(f"Would you like to compare {country} to another country of your choice? Y/N\n Type here: ")
                if choice != "Y" and choice != "y" and choice != "yes" and choice != "N" and choice != "n" and choice != "no":
                    tui.error("Incorrect choice, please try again. Your options are Y or N")
                else:
                    if choice == "N" or choice == "n" or choice == "no":
                        stop2 = 1
                        return final_list
                    elif choice == "Y" or choice == "y" or choice == "yes":
                        while stop3 == 0:
                            second_country = tui.get_a_country_for_visualisation()
                            if check_if_a_country_is_in_db(second_country) == False:
                                tui.error("No such country in the database, please try again")
                            else:
                                stop3 = 1
                                stop2 = 1
                                second_country_value = [second_country]
                                sql_query = "SELECT SUM(statistics.confirmed) as sum_confirmed, SUM(statistics.deaths) as sum_deaths, SUM(statistics.recovered) as sum_recovered, dates.observation_date, countries_regions.country_region FROM dates INNER JOIN records ON dates.dates_id = records.dates_id INNER JOIN countries_regions ON records.country_region_id=countries_regions.country_region_id INNER JOIN statistics ON records.record_id=statistics.record_id WHERE countries_regions.country_region=? GROUP BY countries_regions.country_region, dates.observation_date ORDER BY dates.observation_date ASC"
                                cursor.execute(sql_query, second_country_value)
                                all_records = cursor.fetchall()
                                final_list.append(all_records)
                                return final_list
    db.close()

#print(number_confirmed_deaths_recovered_by_obsdate_country())