"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

from datetime import datetime

def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'COVID-19 (January) Data'.
    The welcome message should contain dashes above and below the title.
    The number of dashes should be equivalent to the number of characters in the title.

    :return: Does not return anything.
    """
    # TO DO: Your code here
    print("-----------------------")
    print("COVID-19 (January) Data")
    print("-----------------------")

#welcome()


def error(msg):
    """
    Task 2: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: A string containing an error message
    :return: Does not return anything
    """
    # TO DO: Your code here
    #error_msg = msg
    print(f"Error! {msg}.")

#error("This is an error message")


def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    '{operation} {status}.'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'has started' if the value of the parameter 'value' is 0
    {status} is 'is in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'has completed' if the value of the parameter 'value' is 100

    :param operation: A string indicating the operation being started
    :param value: An integer indicating the amount of progress made
    :return: Does not return anything
    """
    # TO DO: Your code here
    if value == 0:
        status = "has started"
        print(f"{operation} {status}.")
    elif value > 0 and value < 100:
        status = f"is in progress ({value}% completed)"
        print(f"{operation} {status}.")
    elif value == 100:
        status = "has completed"
        print(f"{operation} {status}.")
    else:
        print("The value needs to be between 0 and 100 (including 0 and 100). Please try again!")

#progress("Operation 1", 0)
#progress("Operation 2", 55)
#progress("Operation 3", 100)
#progress("Operation 4", -10)


def menu(variant=0):
    """
    Task 4: Display a menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a menu with the following options
    should be displayed:

    '[1] Process Data', '[2] Query Database', '[3] Visualise Data' and '[4] Exit'

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
    '[4] Summarise Records'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Setup database',
    '[2] Retrieve all countries in alphabetical order from the database',
    '[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database',
    '[4] Retrieve top 5 countries for confirmed cases from the database from the database',
    '[5] Retrieve top 5 countries for deaths for specific observation dates form the database'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: nothing if invalid selection otherwise an integer for a valid selection
    """
    # TO DO: Your code here
    if variant == 0 or variant == "":
        user_response = int(input("[1] Process Data\n"
                                  "[2] Query Database\n"
                                  "[3] Visualise Data\n"
                                  "[4] Exit\n"
                                  "Type here: "))
        if (user_response > 4 or user_response < 1):
            return "Error! Please insert an appropriate value (your options are: 1, 2, 3 & 4). "
        else:
            return user_response
    elif variant == 1:
        user_response = int(input("[1] Record by Serial Number\n"
                                  "[2] Records by Observation Date\n"
                                  "[3] Group Records by Country/Region\n"
                                  "[4] Summarise Records\n"
                                  "Type here: "))
        if (user_response > 4 or user_response < 1):
            return "Error! Please insert an appropriate value (your options are: 1, 2, 3 & 4). "
        else:
            return user_response
    elif variant == 2:
        user_response = int(input("[1] Setup database\n"
              "[2] Retrieve all countries in alphabetical order from the database\n"
              "[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database\n"
              "[4] Retrieve top 5 countries for confirmed cases from the database from the database\n"
              "[5] Retrieve top 5 countries for deaths for specific observation dates form the database\nType here: "))
        if (user_response > 5 or user_response < 1):
            return "Error! Please insert an appropriate value (your options are: 1, 2, 3, 4 & 5). "
        else:
            return user_response
    elif variant == 3:
        user_response = int(input("[1] Country/Region Pie Chart\n"
                                  "[2] Observations Chart\n"
                                  "[3] Animated Summary\n"
                                  "Type here: "))
        if (user_response > 3 or user_response < 1):
            return "Error! Please insert an appropriate value (your options are: 1, 2 & 3). "
        else:
            return user_response
    else:
        return "Error! Please re-insert an appropriate value (your options are: enter, 0, 1, 2 & 3)."

#print(menu())
#print(menu(variant=1))
#print(menu(variant=2))
#print(menu(variant=3))
#print(menu(variant=66))


def total_records(num_records):
    """
    Task 5: Display the total number of records in the data set.

    The function should display a message in the following format:

    "There are {num_records} records in the data set."

    Where {num_records} is the value of the parameter passed to this function

    :param num_records: the total number of records in the data set
    :return: Does not return anything
    """
    # TO DO: Your code here
    print(f"There are {num_records} records in the data set.")

#total_records(513)


def serial_number():
    """
    Task 6: Read in the serial number of a record and return the serial number.

    The function should ask the user to enter a serial number for a record e.g. 189
    The function should then read in and return the user's response as an integer.

    :return: the serial number for a record
    """
    # TO DO: Your code here
    serial_number_user = input("Please enter a serial number for a record: ")
    return int(serial_number_user)

#print(serial_number())


#-------ADDITIONAL FUNCTION------------ // Validates the inserted date //// Task 7
def validate_date(date):
    try:
        if date != datetime.strptime(date, "%m/%d/%Y").strftime('%m/%d/%Y'):
            raise ValueError
        return True
    except ValueError:
        return False
#print(validate_date("02/30/2020"))


def observation_dates():
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format mm/dd/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    # TO DO: Your code here
    print("Please enter some observation dates in format MM/DD/YYYY. When you want to stop, type 'stop'.")
    obs_dates = []
    stop = 1
    while stop == 1:
        user_input = input()
        if user_input == "stop":
            stop = 0
        else:
            if validate_date(user_input) == False:
                error("Not a valid date, please add a different date")
            else:
                obs_dates.append(user_input)
    return obs_dates

#print(observation_dates())


def display_record(record, cols=None):
    """
    Task 8: Display a record. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the record will be displayed.

    The parameter record is a list of values e.g. [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    The parameter cols is a list of column indexes e.g. [0,3,5]
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    ['01/22/2020','Mainland China']

    E.g. if cols is [0,1,4] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    [1,'01/22/2020','1/22/2020 17:00']

    E.g. if cols is an empty list or None then all the values will be displayed
    [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]

    :param record: A list of data values for a record
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TO DO: Your code here
    outcome = []
    for rec in range(len(record)):
        #print(rec)
        if cols is None or cols == 0 or cols == []:
            outcome.append(record[rec])
        else:
            for col in cols:
                #print(col)
                if rec == col:
                    #print(record[rec])
                    outcome.append(record[rec])
    print(outcome)

#Task 8: Display a record. Only the data for the specified column indexes will be displayed.
#display_record([1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0], [1,3]) #print: ['01/22/2020','Mainland China']
#display_record([1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0], cols=0)
#display_record([1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0], [])
#display_record([1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0], cols=None)
#display_record([1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0], [0,1,4]) #print: [1,'01/22/2020','1/22/2020 17:00']


def display_records(records, cols=None):
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a record will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TO DO: Your code here
    #creating my 2 empty lists for the print outcome
    outcome = []
    outcome_list = []
    #if cols is an empty list or None then all values for the record should be displayed.
    if cols is None or cols == 0 or cols == []:
        for line in records:
            print(line)
    else:
        #need to know how many list i have within the list
        for rec in range(len(records)):
            #print("rec=", rec)  -> added for the purposes of testing
            #print("records[rec]= ", records[rec])  -> added for the purposes of testing
            #going into each individual list within the main list
            for rec2 in range(len(records[rec])):
                #print("rec2= ", rec2) -> added for the purposes of testing
                #going into cols list
                for col in cols:
                    #print("col=", col) -> added for the purposes of testing
                    #condition and appending the list to the middle outcome list
                    if rec2 == col:
                        #print(records[rec][rec2]) -> added for the purposes of testing
                        outcome_list.append(records[rec][rec2])
                        #print("outcome_list=", outcome_list) -> added for the purposes of testing
            #adding it to the main outcome list
            outcome.append(outcome_list)
            #setting it back to empty
            outcome_list = []
        #print(outcome)
        for line in outcome:
            print(line)

#display_records([[1,'01/22/2020','Anhui'], [2,'02/22/2020','Anhui2'], [3,'03/22/2020','Anhui3']], cols=None)
#display_records([[111111,'01/22/2020','Anhui'], [22222,'02/22/2020','Anhui2'], [33333,'03/22/2020','Anhui3']], cols=0)
#display_records([[1,'01/22/2020'], [2,'02/22/2020'], [3,'03/22/2020']], cols=None)
#print("========================================")
#display_records([['11111111','01/22/2020','Anhui'], ['222222222','02/22/2020','Anhui2']], [0,2])
#display_records([['1','01/22/2020','Anhui'], ['2','02/22/2020','Anhui2'], ['3','03/22/2020','Anhui3']], [0,1])


#------------------ADDITIONAL FUNCTIONS---------------------

#Additional functions [1]->[4]: Summarise Records //// for Task 15
#created for a more pleasant display of the results
def  display_the_summary(records):
    for rec in range(len(records)):
        print(f"Location: {records[rec][0]} -> confirmed cases={records[rec][1]}, deaths={records[rec][2]}, recovered={records[rec][3]}")

#display_the_summary([['Mainland China', 38340, 905, 838], ['Hong Kong', 65, 0, 0], ['Macau', 46, 0, 0], ['Taiwan', 52, 0, 0], ['US', 37, 0, 0], ['Japan', 55, 0, 6], ['Thailand', 96, 0, 49], ['South Korea', 36, 0, 0], ['China', 0, 0, 0], ['Kiribati', 0, 0, 0], ['Singapore', 53, 0, 0], ['Philippines', 2, 0, 0], ['Malaysia', 38, 0, 0], ['Vietnam', 18, 0, 0], ['Australia', 41, 0, 4], ['Mexico', 0, 0, 0], ['Brazil', 0, 0, 0], ['Colombia', 0, 0, 0], ['France', 30, 0, 0], ['Nepal', 7, 0, 0], ['Canada', 12, 0, 0], ['Cambodia', 5, 0, 0], ['Sri Lanka', 5, 0, 0], ['Ivory Coast', 1, 0, 0], ['Germany', 17, 0, 0], ['Finland', 3, 0, 0], ['United Arab Emirates', 12, 0, 0], ['India', 2, 0, 0], ['Italy', 2, 0, 0], ['UK', 2, 0, 0], ['Russia', 2, 0, 0], ['Sweden', 1, 0, 0]])



#Additional functions [2]->[3]: Retrieve confirmed cases, deaths and recoveries for an observation from the database //// for Task 21
#created for a more pleasant display of the results
def display_c_d_r_for_sno(list):
    print(f"Results for the serial number={list[0]} are: confirmed cases={list[1]}, deaths={list[2]} & recovered={list[3]}.")



#Additional functions [2]->[4]: Retrieve top 5 countries for confirmed cases from the database from the database //// for Task 21
#created for a more pleasant display of the results
def display_retrieve_info_top5_countries_confirmed_cases(list):
    for val in range(0, len(list)-1, 2):
        print(f"{list[val]}: {list[val+1]} confirmed cases")



#Additional functions Animated Summary //// for Task 30
def get_a_country_for_visualisation():
    print("Please insert a country for visualising insights regarding it (eg: Mainland China, Thailand, Japan, etc): ")
    country = str(input())
    #Makeing each word capitalised for when we check if it exists inside the db
    return country.title()
