# Process & Manage Covid-19 Dataset
The task was to **create a software application that can be used to process and manage data related to the COVID-19 observations.**


## The project's requirements:

a) The system will present the user with a text-based user interface through which a user will select options to load the data, process the data, persist the data and visualise the data.

b) The system will load the data from a CSV file into memory.

c) The system will allow the user to process the loaded data for certain scenarios.

d) The system will allow the user to persist the data to a database. The data should be stored using an appropriate database model. You are required to design the database model.

e) The system will allow the user to utilise the data stored in the database to perform certain queries:

f) The system will allow the user to visualise the data stored in the database for certain scenarios.


### The application's menu:
[1] Process Data
* [1] Record by Serial Number
* [2] Records by Observation Date
* [3] Group Records by Country/Region
* [4] Summarise Records

[2] Query Database
* [1] Setup database
* [2] Retrieve all countries in alphabetical order from the database
* [3] Retrieve confirmed cases, deaths and recoveries for an observation from the database
* [4] Retrieve top 5 countries for confirmed cases from the database from the database
* [5] Retrieve top 5 countries for deaths for specific observation dates form the database

[3] Visualise Data
* [1] Country/Region Pie Chart
* [2] Observations Chart
* [3] Animated Summary

[4] Exit


## Description of each module:
- _**Tui**_ – This module provides a text-user interface for the software application. All communication with the user (reading user input or displaying text output) is performed using functions in this module.
- _**Process**_ – This module contains several user-defined functions that can be utilised to process the data. The functions will take suitable parameters and return results consisting of processed data.
- _**Database**_ – This module provides a means of persisting the data to a local database and subsequently querying the database.
- _**Visual**_ – This module provides the visual interface for the software application and contains functions used to display suitable visual outputs such as charts.
- _**Main**_ – This module contains the main logic for the software application and utilises the other modules.

### Tasks breakdown:
Module | Tasks | 
--- | --- | 
_tui_ | 1 - 9 |
_process_ | 16 - 20 |
_database_ | 22 – 26 |
_visual_ | 28 – 30 |
_main_ | 10 – 15, 21, 27, 31 & 32 |

## Proposed Database Model
![alt text](https://github.com/denisect/covid_19_dataset/blob/main/proposed_database_model.PNG?raw=true)
