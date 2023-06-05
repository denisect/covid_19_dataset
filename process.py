"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""
"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
-TASK 16: Retrieve the total number of records that have been loaded.
-TASK 17: Retrieve a record with the serial number as specified by the user.
-TASK 18: Retrieve the records for the observation dates as specified by the user.
-TASK 19: Retrieve all of the records grouped by the country/region.
-TASK 20: Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries
"""
# TO DO: Your code here
import tui

#TASK 16: Retrieve the total number of records that have been loaded.
def total_no_of_rec_loaded(list_of_records):
    tot_no_rec = len(list_of_records)
    #print(tot_no_rec)
    return tot_no_rec

#print(total_no_of_rec_loaded([['1', '01/22/2020', 'Anhui', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['2', '01/22/2020', 'Beijing', 'Mainland China', '1/22/2020 17:00', '14', '0', '0'], ['3', '01/22/2020', 'Chongqing', 'Mainland China', '1/22/2020 17:00', '6', '0', '0'], ['4', '01/22/2020', 'Fujian', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['5', '01/22/2020', 'Gansu', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['6', '01/22/2020', 'Guangdong', 'Mainland China', '1/22/2020 17:00', '26', '0', '0'], ['7', '01/22/2020', 'Guangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['8', '01/22/2020', 'Guizhou', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['9', '01/22/2020', 'Hainan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['10', '01/22/2020', 'Hebei', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['11', '01/22/2020', 'Heilongjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['12', '01/22/2020', 'Henan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['13', '01/22/2020', 'Hong Kong', 'Hong Kong', '1/22/2020 17:00', '0', '0', '0'], ['14', '01/22/2020', 'Hubei', 'Mainland China', '1/22/2020 17:00', '444', '17', '28'], ['15', '01/22/2020', 'Hunan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['16', '01/22/2020', 'Inner Mongolia', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['17', '01/22/2020', 'Jiangsu', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['18', '01/22/2020', 'Jiangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['19', '01/22/2020', 'Jilin', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['20', '01/22/2020', 'Liaoning', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['21', '01/22/2020', 'Macau', 'Macau', '1/22/2020 17:00', '1', '0', '0'], ['22', '01/22/2020', 'Ningxia', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['23', '01/22/2020', 'Qinghai', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['24', '01/22/2020', 'Shaanxi', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['25', '01/22/2020', 'Shandong', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['26', '01/22/2020', 'Shanghai', 'Mainland China', '1/22/2020 17:00', '9', '0', '0'], ['27', '01/22/2020', 'Shanxi', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['28', '01/22/2020', 'Sichuan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['29', '01/22/2020', 'Taiwan', 'Taiwan', '1/22/2020 17:00', '1', '0', '0'], ['30', '01/22/2020', 'Tianjin', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['31', '01/22/2020', 'Tibet', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['32', '01/22/2020', 'Washington', 'US', '1/22/2020 17:00', '1', '0', '0'], ['33', '01/22/2020', 'Xinjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['34', '01/22/2020', 'Yunnan', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['35', '01/22/2020', 'Zhejiang', 'Mainland China', '1/22/2020 17:00', '10', '0', '0'], ['36', '01/22/2020', '', 'Japan', '1/22/2020 17:00', '2', '0', '0'], ['37', '01/22/2020', '', 'Thailand', '1/22/2020 17:00', '4', '0', '2'], ['38', '01/22/2020', '', 'South Korea', '1/22/2020 17:00', '1', '0', '0'], ['39', '01/22/2020', 'Unknown', 'China', '1/22/2020 17:00', '0', '0', '0'], ['40', '01/22/2020', '', 'Kiribati', '1/22/2020 17:00', '0', '0', '0']]))


#TASK 17: Retrieve a record with the serial number as specified by the user.
def record_by_serial_no(list_of_records):
    result = ""
    serial_no = tui.serial_number()
    for values in range(len(list_of_records)):
        if serial_no == int(list_of_records[values][0]):
            result = tui.display_record(list_of_records[values], cols=None)
    if result == "":
        return tui.error("A record with the serial number inserted is not found")
    else:
        return result


#TASK 18: Retrieve the records for the observation dates as specified by the user.
def multiple_rec_by_obs_dates(list_of_records):
    results = []
    obs_dates = tui.observation_dates()
    for values in range(len(list_of_records)):
        for date in range(len(obs_dates)):
            #print(obs_dates[date])
            #print(list_of_records[values][1])
            if list_of_records[values][1] == obs_dates[date]:
                results.append(list_of_records[values])
                #print("obs_date[date]", obs_dates[date])
    if results == []:
        return "Not found"
    else:
        return results


#TASK 19:Retrieve all of the records grouped by the country/region.
def group_recs_by_country_region(list_of_records):
    #get a list that contains all the country/regions from the data
    country_region = []
    for values in range(len(list_of_records)):
        country_region.append(list_of_records[values][3])

    #remove duplicates from a list
    country_region = list(dict.fromkeys(country_region))

    #print(country_region)
    final_list = []
    #loop through the unique list to re-arrange and append the records
    for i in range(len(country_region)):
        for values in range(len(list_of_records)):
            if list_of_records[values][3] == country_region[i]:
                final_list.append(list_of_records[values])
    return final_list

#print(group_recs_by_country_region([['1', '01/22/2020', 'Anhui', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['2', '01/22/2020', 'Beijing', 'Mainland China', '1/22/2020 17:00', '14', '0', '0'], ['3', '01/22/2020', 'Chongqing', 'Mainland China', '1/22/2020 17:00', '6', '0', '0'], ['4', '01/22/2020', 'Fujian', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['5', '01/22/2020', 'Gansu', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['6', '01/22/2020', 'Guangdong', 'Mainland China', '1/22/2020 17:00', '26', '0', '0'], ['7', '01/22/2020', 'Guangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['8', '01/22/2020', 'Guizhou', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['9', '01/22/2020', 'Hainan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['10', '01/22/2020', 'Hebei', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['11', '01/22/2020', 'Heilongjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['12', '01/22/2020', 'Henan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['13', '01/22/2020', 'Hong Kong', 'Hong Kong', '1/22/2020 17:00', '0', '0', '0'], ['14', '01/22/2020', 'Hubei', 'Mainland China', '1/22/2020 17:00', '444', '17', '28'], ['15', '01/22/2020', 'Hunan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['16', '01/22/2020', 'Inner Mongolia', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['17', '01/22/2020', 'Jiangsu', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['18', '01/22/2020', 'Jiangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['19', '01/22/2020', 'Jilin', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['20', '01/22/2020', 'Liaoning', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['21', '01/22/2020', 'Macau', 'Macau', '1/22/2020 17:00', '1', '0', '0'], ['22', '01/22/2020', 'Ningxia', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['23', '01/22/2020', 'Qinghai', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['24', '01/22/2020', 'Shaanxi', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['25', '01/22/2020', 'Shandong', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['26', '01/22/2020', 'Shanghai', 'Mainland China', '1/22/2020 17:00', '9', '0', '0'], ['27', '01/22/2020', 'Shanxi', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['28', '01/22/2020', 'Sichuan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['29', '01/22/2020', 'Taiwan', 'Taiwan', '1/22/2020 17:00', '1', '0', '0'], ['30', '01/22/2020', 'Tianjin', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['31', '01/22/2020', 'Tibet', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['32', '01/22/2020', 'Washington', 'US', '1/22/2020 17:00', '1', '0', '0'], ['33', '01/22/2020', 'Xinjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['34', '01/22/2020', 'Yunnan', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['35', '01/22/2020', 'Zhejiang', 'Mainland China', '1/22/2020 17:00', '10', '0', '0'], ['36', '01/22/2020', '', 'Japan', '1/22/2020 17:00', '2', '0', '0'], ['37', '01/22/2020', '', 'Thailand', '1/22/2020 17:00', '4', '0', '2'], ['38', '01/22/2020', '', 'South Korea', '1/22/2020 17:00', '1', '0', '0'], ['39', '01/22/2020', 'Unknown', 'China', '1/22/2020 17:00', '0', '0', '0'], ['40', '01/22/2020', '', 'Kiribati', '1/22/2020 17:00', '0', '0', '0']]))


#TASK 20: Retrieve a summary of all of the records. This should include the following information for each country/region:
    # the total number of confirmed cases
    # the total number of deaths
    # the total number of recoveries
def summary_all_records(list_of_records):
    #get a list that contains all the country/regions from the data
    country_region = []
    for values in range(len(list_of_records)):
        country_region.append(list_of_records[values][3])

    #remove duplicates from a list
    country_region = list(dict.fromkeys(country_region))

    #print(country_region)
    final_list = []
    #loop through the unique list to do the calculations
    for i in range(len(country_region)):
        confirmed_cases = 0
        deaths = 0
        recovered = 0
        for values in range(len(list_of_records)):
            if list_of_records[values][3] == country_region[i]:
                prelist = []
                location = country_region[i]
                prelist.append(location)
                confirmed_cases = confirmed_cases+int(list_of_records[values][5])
                prelist.append(confirmed_cases)
                deaths = deaths+int(list_of_records[values][6])
                prelist.append(deaths)
                recovered = recovered+int(list_of_records[values][7])
                prelist.append(recovered)
        final_list.append(prelist)
    return final_list

#print(summary_all_records([['Mainland China', '1', '0', '0'], ['Mainland China', '14', '0', '0'], ['Mainland China', '6', '0', '0']]))
#['4', '01/22/2020', 'Fujian', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['5', '01/22/2020', 'Gansu', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['6', '01/22/2020', 'Guangdong', 'Mainland China', '1/22/2020 17:00', '26', '0', '0'], ['7', '01/22/2020', 'Guangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['8', '01/22/2020', 'Guizhou', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['9', '01/22/2020', 'Hainan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['10', '01/22/2020', 'Hebei', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['11', '01/22/2020', 'Heilongjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['12', '01/22/2020', 'Henan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['13', '01/22/2020', 'Hong Kong', 'Hong Kong', '1/22/2020 17:00', '0', '0', '0'], ['14', '01/22/2020', 'Hubei', 'Mainland China', '1/22/2020 17:00', '444', '17', '28'], ['15', '01/22/2020', 'Hunan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['16', '01/22/2020', 'Inner Mongolia', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['17', '01/22/2020', 'Jiangsu', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['18', '01/22/2020', 'Jiangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['19', '01/22/2020', 'Jilin', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['20', '01/22/2020', 'Liaoning', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['21', '01/22/2020', 'Macau', 'Macau', '1/22/2020 17:00', '1', '0', '0'], ['22', '01/22/2020', 'Ningxia', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['23', '01/22/2020', 'Qinghai', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['24', '01/22/2020', 'Shaanxi', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['25', '01/22/2020', 'Shandong', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['26', '01/22/2020', 'Shanghai', 'Mainland China', '1/22/2020 17:00', '9', '0', '0'], ['27', '01/22/2020', 'Shanxi', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['28', '01/22/2020', 'Sichuan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['29', '01/22/2020', 'Taiwan', 'Taiwan', '1/22/2020 17:00', '1', '0', '0'], ['30', '01/22/2020', 'Tianjin', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['31', '01/22/2020', 'Tibet', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['32', '01/22/2020', 'Washington', 'US', '1/22/2020 17:00', '1', '0', '0'], ['33', '01/22/2020', 'Xinjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['34', '01/22/2020', 'Yunnan', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['35', '01/22/2020', 'Zhejiang', 'Mainland China', '1/22/2020 17:00', '10', '0', '0'], ['36', '01/22/2020', '', 'Japan', '1/22/2020 17:00', '2', '0', '0'], ['37', '01/22/2020', '', 'Thailand', '1/22/2020 17:00', '4', '0', '2'], ['38', '01/22/2020', '', 'South Korea', '1/22/2020 17:00', '1', '0', '0'], ['39', '01/22/2020', 'Unknown', 'China', '1/22/2020 17:00', '0', '0', '0'], ['40', '01/22/2020', '', 'Kiribati', '1/22/2020 17:00', '0', '0', '0']]))

#print(summary_all_records([['1', '01/22/2020', 'Anhui', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['2', '01/22/2020', 'Beijing', 'Mainland China', '1/22/2020 17:00', '14', '0', '0'], ['3', '01/22/2020', 'Chongqing', 'Mainland China', '1/22/2020 17:00', '6', '0', '0'], ['4', '01/22/2020', 'Fujian', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['5', '01/22/2020', 'Gansu', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['6', '01/22/2020', 'Guangdong', 'Mainland China', '1/22/2020 17:00', '26', '0', '0'], ['7', '01/22/2020', 'Guangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['8', '01/22/2020', 'Guizhou', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['9', '01/22/2020', 'Hainan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['10', '01/22/2020', 'Hebei', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['11', '01/22/2020', 'Heilongjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['12', '01/22/2020', 'Henan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['13', '01/22/2020', 'Hong Kong', 'Hong Kong', '1/22/2020 17:00', '0', '0', '0'], ['14', '01/22/2020', 'Hubei', 'Mainland China', '1/22/2020 17:00', '444', '17', '28'], ['15', '01/22/2020', 'Hunan', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['16', '01/22/2020', 'Inner Mongolia', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['17', '01/22/2020', 'Jiangsu', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['18', '01/22/2020', 'Jiangxi', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['19', '01/22/2020', 'Jilin', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['20', '01/22/2020', 'Liaoning', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['21', '01/22/2020', 'Macau', 'Macau', '1/22/2020 17:00', '1', '0', '0'], ['22', '01/22/2020', 'Ningxia', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['23', '01/22/2020', 'Qinghai', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['24', '01/22/2020', 'Shaanxi', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['25', '01/22/2020', 'Shandong', 'Mainland China', '1/22/2020 17:00', '2', '0', '0'], ['26', '01/22/2020', 'Shanghai', 'Mainland China', '1/22/2020 17:00', '9', '0', '0'], ['27', '01/22/2020', 'Shanxi', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['28', '01/22/2020', 'Sichuan', 'Mainland China', '1/22/2020 17:00', '5', '0', '0'], ['29', '01/22/2020', 'Taiwan', 'Taiwan', '1/22/2020 17:00', '1', '0', '0'], ['30', '01/22/2020', 'Tianjin', 'Mainland China', '1/22/2020 17:00', '4', '0', '0'], ['31', '01/22/2020', 'Tibet', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['32', '01/22/2020', 'Washington', 'US', '1/22/2020 17:00', '1', '0', '0'], ['33', '01/22/2020', 'Xinjiang', 'Mainland China', '1/22/2020 17:00', '0', '0', '0'], ['34', '01/22/2020', 'Yunnan', 'Mainland China', '1/22/2020 17:00', '1', '0', '0'], ['35', '01/22/2020', 'Zhejiang', 'Mainland China', '1/22/2020 17:00', '10', '0', '0'], ['36', '01/22/2020', '', 'Japan', '1/22/2020 17:00', '2', '0', '0'], ['37', '01/22/2020', '', 'Thailand', '1/22/2020 17:00', '4', '0', '2'], ['38', '01/22/2020', '', 'South Korea', '1/22/2020 17:00', '1', '0', '0'], ['39', '01/22/2020', 'Unknown', 'China', '1/22/2020 17:00', '0', '0', '0'], ['40', '01/22/2020', '', 'Kiribati', '1/22/2020 17:00', '0', '0', '0']]))