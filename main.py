"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any database related querying should be done using the appropriate functions the module 'database'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# Task 10: Import required modules
# TO DO: Your code here
import tui
import csv
import process
import database
import visual

# Added to handle the sqlite3 error
# 1. when wanting to setup the database multiple times - sqlite3.IntegrityError
# 2. when wanting to first run any other options prior setting up the database - sqlite3.OperationalError
import sqlite3

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TO DO: Your code here
covid_records = []

def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TO DO: Your code here
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    # TO DO: Your code here
    tui.progress("Data loading operation", 0)
    file = "../AE1/data/covid_19_data.csv"
    try:
        with open(file) as file_path:
            csv_reader_var = csv.reader(file_path)
            headings = next(csv_reader_var)
            for values in csv_reader_var:
                #print(values)
                covid_records.append(values)
        #print(covid_records)
    except IOError:
        print("Cannot read file.")

    tui.total_records(len(covid_records))
    #print(covid_records)
    tui.progress("Data loading operation", 100)

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TO DO: Your code here
        user_input_main_menu = tui.menu(variant=0)

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary  = create a new function in tui that will display it properly
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TO DO: Your code here
        if user_input_main_menu == 1:
            tui.progress("Data processing operation", 0)
            user_input_pro_data = tui.menu(variant=1)
            #[1] Record by Serial Number
            if user_input_pro_data == 1:
                tui.progress("Record retrieval process", 0)
                process.record_by_serial_no(covid_records)
                print(headings)
                tui.progress("Record retrieval process", 100)
            #[2] Records by Observation Date
            elif user_input_pro_data == 2:
                tui.progress("Record retrieval process", 0)
                x = process.multiple_rec_by_obs_dates(covid_records)
                if x == "Not found":
                    tui.error("No records found")
                else:
                    print(headings)
                    tui.display_records(x, cols=None)
                tui.progress("Record retrieval process", 100)
            #[3] Group Records by Country/Region
            elif user_input_pro_data == 3:
                tui.progress("The grouping process", 0)
                print(headings)
                tui.display_records(process.group_recs_by_country_region(covid_records), cols=0)
                tui.progress("The grouping process", 100)
            #[4] Summarise Records
            elif user_input_pro_data == 4:
                tui.progress("The summary process", 0)
                tui.display_the_summary(process.summary_all_records(covid_records))
                tui.progress("The summary process", 100)
            else:
                tui.error("Invalid option, please try again. Your options are: 1, 2, 3 & 4")
            tui.progress("Data processing operation", 100)

        # Task 21: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what querying is to be done.
        #   - call the appropriate function in the module 'database' to retrieve the results
        #   - call the appropriate function in the module 'tui' to display the results
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has completed.
        # TO DO: Your code here
        elif user_input_main_menu == 2:
            tui.progress("Database querying operation", 0)
            user_input_pro_data = tui.menu(variant=2)
            #[1] Setup database
            #This try-except is added to prevent the user in running any other options before setting up the database
            try:
                if user_input_pro_data == 1:
                    #If this try-except is not added, then when wanting to setup the database again an error will pop-up
                    #This is added to avoid that error which is caused by unique constraint
                    try:
                        tui.progress("Database setting up operation", 0)
                        database.setup_database(covid_records)
                        tui.progress("Database setting up operation", 100)
                    except sqlite3.IntegrityError:
                        print("You have already set up the database.")
                #[2] Retrieve all countries in alphabetical order from the database
                elif user_input_pro_data == 2:
                    tui.display_records(database.unique_countries_alphabetical_order(), cols=0)
                #[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database
                elif user_input_pro_data == 3:
                    tui.display_c_d_r_for_sno(database.number_confirmed_deaths_recovered_by_sno())
                #[4] Retrieve top 5 countries for confirmed cases from the database from the database
                elif user_input_pro_data == 4:
                    tui.display_retrieve_info_top5_countries_confirmed_cases(database.retrieve_info_top5_countries_confirmed_cases())
                #[5] Retrieve top 5 countries for deaths for specific observation dates form the database
                elif user_input_pro_data == 5:
                    tui.display_records(database.retrieve_info_top5_countries_deaths_obsdate(), cols=0)
                else:
                    tui.error("Invalid option, please try again. Your options are: 1, 2, 3, 4 & 5")
            except sqlite3.OperationalError:
                print("You need to set up the database first ([2] Query Database -> [1] Setup database) to be able to run this option.")
            tui.progress("Database querying operation", 100)

        # Task 27: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TO DO: Your code here
        elif user_input_main_menu == 3:
            tui.progress("Database visualisation operation", 0)
            user_input_pro_data = tui.menu(variant=3)
            try:
                #Country/Region Pie Chart
                if user_input_pro_data == 1:
                    visual.top5_countries_confirmed_cases_piechart()
                #Observations Chart
                elif user_input_pro_data == 2:
                    visual.top5_countries_death_specific_dates_barchart()
                #Animated Summary
                elif user_input_pro_data == 3:
                    visual.visualisation_cdr_cases_overtime_country()
                else:
                    tui.error("Invalid option, please try again. Your options are: 1, 2 & 3")
            except sqlite3.OperationalError:
                print("You need to set up the database first ([2] Query Database -> [1] Setup database) to be able to run this option.")
            tui.progress("Database visualisation operation", 100)
        # Task 31: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TO DO: Your code here
        elif user_input_main_menu == 4:
            print("Goodbye!")
            break
        # Task 32: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TO DO: Your code here
        else:
            tui.error("Invalid option, please try again! Your options are: 1, 2, 3 & 4")

if __name__ == "__main__":
    run()
