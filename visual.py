"""
This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""
"""
Task 28 - 30: Write suitable functions to visualise the data as follows:

-TASK 28: Display the top 5 countries for confirmed cases using a pie chart
-TASK 29: Display the top 5 countries for death for specific dates using a bar chart
-TASK 30: Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country/countries.

Each function for the above should utilise the functions in the module 'database' to retrieve any data.
You may add additional methods to the module 'database' if needed. Each function should then visualise
the data using Matplotlib.
"""

# TO DO: Your code here
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import database

#TASK 28: Display the top 5 countries for confirmed cases using a pie chart
def top5_countries_confirmed_cases_piechart():
    values = database.retrieve_info_top5_countries_confirmed_cases()
    x = []
    y = []
    sum_y = 0
    for val in range(0, len(values)-1, 2):
        x.append(values[val])
        y.append(values[val+1])
        #getting the sum to be able to calculate the percentages
        sum_y = sum_y + values[val+1]

    #calculating the percentage for each value in the y list and adding it to a new list
    percentage_y_list = []
    for i in y:
        percentage_y = round((i * 100 / sum_y), 2)
        percentage_y_list.append(percentage_y)
        #print(percentage_y)
    #concatenating the x values (country labels) with the corresponding percentage (from the above list)
    new_x = []
    for i in range(len(x)):
        #print(x[i], percentage_y_list[i])
        new_x.append(f"{x[i]}, {percentage_y_list[i]}%")
    #print(new_x)
    colours = ['pink', 'lightskyblue', 'yellowgreen', 'gold', 'violet']
    plt.title("Top 5 countries for confirmed cases")
    plt.pie(y, shadow=True, colors=colours)
    plt.legend(new_x, loc="lower left")
    plt.show()

#top5_countries_confirmed_cases_piechart()


#TASK 29: Display the top 5 countries for death for specific dates using a bar chart
def top5_countries_death_specific_dates_barchart():
    values = database.retrieve_info_top5_countries_deaths_obsdate()
    #values=[['Obs date: 01/22/2020', 'Mainland China', 100, 'Hong Kong', 80, 'US', 75, 'Japan', 55, 'Thailand', 14], ['Obs date: 01/24/2020', 'Mainland China', 125, 'Thailand', 84, 'Japan', 75, 'Hong Kong', 60, 'US', 5]]
    dates = []
    country_values = []
    deaths_values = []
    for value in values:
        country = []
        deaths = []
        dates.append(value[0])
        #print("value=",value)
        for val in range(1, len(value)-1, 2):
            #print("value[val=", value[val])
            country.append(value[val])
            deaths.append(value[val + 1])
        country_values.append(country)
        deaths_values.append(deaths)
    # print("dates=",dates)
    # print("country_values=",country_values)
    # print("deaths_values=",deaths_values)
    plot_number = len(dates)
    #print(plot_number)
    if plot_number == 1:
        fig = plt.figure()
        plt.title("Top 5 countries for death for specific dates")
        plt.bar(country_values[0], deaths_values[0], color='lightskyblue')
        plt.xlabel(dates[0])
    else:
        fig, ax = plt.subplots(plot_number)
        ax[0].set_title("Top 5 countries for death for specific dates")
        for i in range(plot_number):
            ax[i].bar(country_values[i], deaths_values[i], color='lightskyblue')
            ax[i].set_xlabel(dates[i])
    plt.tight_layout()
    plt.show()

#top5_countries_death_specific_dates_barchart()

"""
01/22/2020
01/24/2020
stop
"""


#TASK 30: Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
#time. This could focus on a specific country/countries.

def animate(frame):
    global axs, values_anim
    #-------------------------- IF ONLY 1 COUNTRY INSERTED---------------
    if len(values_anim) == 1:
        c_1 = []
        d_1 = []
        r_1 = []
        dates_1 = []
        country_1 = []
        for i in range(0, 1, 1):
            for j in range(len(values_anim[i])):
                c_1.append(values_anim[i][j][0]) #basically getting only a list of confirmed cases for the first country
                d_1.append(values_anim[i][j][1])
                r_1.append(values_anim[i][j][2])
                dates_1.append(values_anim[i][j][3])
                country_1.append(values_anim[i][j][4])
        # print("c_1=",c_1)
        # print("d_1=",d_1)
        # print("r_1=",r_1)
        # print("dates_1=",dates_1)
        #c_1=[459, 444, 553, 761, 1058, 2459, 3444, 4553, 5761, 6058]
        #d_1=[17, 17, 25, 40, 52, 117, 217, 525, 240, 152]
        #r_1=[28, 28, 31, 32, 42, 128, 228, 331, 742, 242]
        #dates_1=['01/22/2020', '01/23/2020', '01/24/2020', '01/25/2020', '01/26/2020', '01/27/2020', '01/28/2020', '01/29/2020', '01/30/2020', '01/31/2020']
        #print(country_1)
        axs.cla()
        axs.set_xlim(0, 9)
        #I have checked in the datafile and I know that confirmed cases is always bigger than deaths and recoveries
        axs.set_ylim(0, max(c_1)+1)
        axs.set_xlabel(country_1[0])
        #print("frame=",frame)
        for label in axs.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)
        for i in range(0,frame+2):
            axs.plot(dates_1[:i], c_1[:i], 'co-')
            axs.plot(dates_1[:i], d_1[:i], 'ro-')
            axs.plot(dates_1[:i], r_1[:i], 'go-')
            #print("i=",i)
            #print("dates[:i]=",dates[:i])
            #print("c[:i]=", c[:i])
        axs.legend(["Confirmed cases","Deaths","Recovered" ], bbox_to_anchor=(1.05, 1.0), loc="upper left", prop={'size': 8})
        axs.set_title('Number of confirmed cases, deaths & \n recovery change over time', size=8)
        fig.tight_layout()

    #--------------------------IF 2 COUNTRY INSERTED---------------
    elif len(values_anim) == 2:
        #------------FIRST PLOT-----------
        c_1 = []
        d_1 = []
        r_1 = []
        dates_1 = []
        country_1 = []
        for i in range(len(values_anim) - 1):
            for j in range(len(values_anim[i])):
                # print("values_anim[i][j][0]", values_anim[i][j][0])
                c_1.append(values_anim[i][j][0])
                d_1.append(values_anim[i][j][1])
                r_1.append(values_anim[i][j][2])
                dates_1.append(values_anim[i][j][3])
                country_1.append(values_anim[i][j][4])
        # print("c_1=",c_1)
        # print("d_1=",d_1)
        # print("r_1=",r_1)
        # print("dates_1=",dates_1)
        axs[0].cla()
        axs[0].set_xlim(0, 9)
        # I have checked in the datafile and I know that confirmed cases is always bigger than deaths and recoveries
        axs[0].set_ylim(0, max(c_1)+1)
        axs[0].set_xlabel(country_1[0])
        # print("frame=",frame)
        for label in axs[0].get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)
        for i in range(0, frame + 2):
            axs[0].plot(dates_1[:i], c_1[:i], 'co-')
            axs[0].plot(dates_1[:i], d_1[:i], 'ro-')
            axs[0].plot(dates_1[:i], r_1[:i], 'go-')
            # print("i=",i)
            # print("dates[:i]=",dates[:i])
            # print("c[:i]=", c[:i])
        axs[0].legend(["Confirmed cases", "Deaths", "Recovered"], bbox_to_anchor=(1.05, 1.0), loc="upper left",
                      prop={'size': 8})
        axs[0].set_title('Number of confirmed cases, deaths & \n recovery change over time', size=8)
        fig.tight_layout()
        #-----------SECOND PLOT-------------
        c_2 = []
        d_2 = []
        r_2 = []
        dates_2 = []
        country_2 = []
        for i in range(1, 2, 1):
            for j in range(len(values_anim[i])):
                c_2.append(values_anim[i][j][0])
                d_2.append(values_anim[i][j][1])
                r_2.append(values_anim[i][j][2])
                dates_2.append(values_anim[i][j][3])
                country_2.append(values_anim[i][j][4])
        # print("c_2=",c_2)
        # print("d_2=",d_2)
        # print("r_2=",r_2)
        # print("dates_2=",dates_2)
        axs[1].cla()
        axs[1].set_xlim(0, 9)

        # I have checked in the datafile and I know that confirmed cases is always bigger than deaths and recoveries
        if max(c_2) > max(c_1):
            axs[1].set_ylim(0, max(c_2)+1)
        elif max(c_1) > max(c_2):
            axs[1].set_ylim(0, max(c_1)+1)

        axs[1].set_xlabel(f"{country_1[0]} VS {country_2[0]}")
        for label in axs[1].get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)
        for i in range(0, frame + 2):
            axs[1].plot(dates_1[:i], c_1[:i], 'co-')
            axs[1].plot(dates_2[:i], c_2[:i], 'c^-')
            axs[1].plot(dates_1[:i], d_1[:i], 'ro-')
            axs[1].plot(dates_2[:i], d_2[:i], 'r^-')
            axs[1].plot(dates_1[:i], r_1[:i], 'go-')
            axs[1].plot(dates_2[:i], r_2[:i], 'g^-')
        axs[1].legend([f"Confirmed cases - {country_1[0]}", f"Confirmed cases - {country_2[0]}", f"Deaths - {country_1[0]}", f"Deaths - {country_2[0]}", f"Recovered - {country_1[0]}", f"Recovered - {country_2[0]}"], bbox_to_anchor=(1.05, 1.0), loc="upper left", prop={'size': 8})
        axs[1].set_title('Number of confirmed cases, deaths & \n recovery change over time', size=8)
        fig.tight_layout()


def clear_function():
    pass

def visualisation_cdr_cases_overtime_country():
    global fig, axs, values_anim
    values_anim = database.number_confirmed_deaths_recovered_by_obsdate_country()
    if len(values_anim) == 1:
        fig, axs = plt.subplots()
    else:
        fig, axs = plt.subplots(len(values_anim))
    my_animat = animation.FuncAnimation(fig,
                                        animate,
                                        frames=10,
                                        interval=1000,
                                        repeat=False,
                                        init_func=clear_function)
    plt.show()

#visualisation_cdr_cases_overtime_country()


"""
colour options: 
colours = ['pink', 'lightskyblue', 'violet', 'yellowgreen', 'red', 'gold', 'blue', 'magenta', 'darkgreen', 'lightcoral', 'yellow', 'grey', 'cyan'] 
"""