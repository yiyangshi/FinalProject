import time
import operator
from help import calculate_list
from help import basic_stats
from help import delay_breakdown
from help import sort_carrier_by_delay_reason
from carrier_dict import carrier_dict

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

with open('Feb.csv') as f:
    lines = f.readlines()



############ Make Initial Table
table = []
for line in lines:
    line = line.strip()
    line = line.split(',')
    del line[-1]
    table.append(line)



############# Clean Up Table
print("Please wait while the file is being cleaned...")
start_time = time.time()

cleaned_table = [[] for x in range(len(table))] ###change to len(table)
cleaned_line = []
i = 0
for line in table: ###change to table
    for element in line:
        while element.startswith('"'):
            element = element[1:]
        while element.endswith('"'):
            element = element[:-1]
        while element.startswith(' '):
            element = element[1:]
        while element.endswith(' '):
            element = element[:-1]
        cleaned_line.append(element)
    cleaned_table[i] = cleaned_line
    cleaned_line = []
    i += 1

end_time=time.time()-start_time
print("Your file is loaded. It took", int(end_time),"seconds to clean your file." )



############### Function 4: Basic Stats
def functionality_4_basic_stats():
    basic_stats_options = """
Calculate max, avg, min delay minutes for a:
1 - Carrier
2 - Departure Airport
0 - Exit
"""
    while True:
        print(basic_stats_options)
        basic_stats_input = input("Please enter a number: ")
        try:
            float(basic_stats_input)
            if float(basic_stats_input) == 1:
                basic_stats(1, cleaned_table)
            elif float(basic_stats_input) == 2:
                basic_stats(2, cleaned_table)
            elif float(basic_stats_input) == 0:
                break
            else:
                print('Invalid Number. Please try again.')
        except:
             print('Invalid. Please enter a number.')



############## Function 5: Delay Breakdown
def functionality_5_delay_breakdown():
    delay_breakdown_options = """
Explore delay reasons for a:
1 - Carrier
2 - Departure Airport
0 - Exit
"""
    while True:
        print(delay_breakdown_options)
        delay_breakdown_input = input("Please enter a number: ")
        try:
            float(delay_breakdown_input)
            if float(delay_breakdown_input) == 1:
                delay_breakdown(1, cleaned_table)
            elif float(delay_breakdown_input) == 2:
                delay_breakdown(2, cleaned_table)
            elif float(delay_breakdown_input) == 0:
                break
            else:
                print('Invalid Number. Please try again.')
        except:
            print('Invalid. Please enter a number.')



############# Function 1: Carriers ranked by percentage of delay
def functionality_1_carrier_rank_percentage_delay():
    total_carrier_count = dict()
    delay_carrier_count = dict()

    for line in cleaned_table[1:]:
        if line[4] in total_carrier_count:
            total_carrier_count[line[4]] += 1
        else:
            total_carrier_count[line[4]] = 1
        try:
            float(line[-6])
            if float(line[-6]) > 0:
                if line[4] in delay_carrier_count:
                    delay_carrier_count[line[4]] += 1
                else:
                    delay_carrier_count[line[4]] = 1
        except:
            continue

    top_carrier = dict()
    for key in total_carrier_count:
        top_carrier[key] = delay_carrier_count[key]/total_carrier_count[key]

    sorted_top_carrier = sorted(top_carrier, key=top_carrier.get, reverse=True)

    print("Carriers Delay Probability: ")
    rank = 1
    for key in sorted_top_carrier:
        print("No.", rank, "  ", int((top_carrier[key])*100), "%","  ", carrier_dict[key])
        rank +=1



################### Function 3: Avg delay time for different day of week
def functionality_3_rank_day():
    total_delay_day = dict()
    count_delay_day = dict()
    avg_delay_day = dict()
    day_number = {'1': 'Mon: ', '2': 'Tue: ', '3': 'Wed: ', '4': 'Thu: ', '5': 'Fri: ', '6': 'Sat: ', '7': 'Sun: '}

    x_axis = []
    y_axis = []

    for line in cleaned_table[1:]:
        try:
            float(line[-6])
            if float(line[-6]) > 0:
                if line[2] in total_delay_day:
                    total_delay_day[line[2]] += float(line[-6])
                    count_delay_day[line[2]] += 1
                else:
                    total_delay_day[line[2]] = float(line[-6])
                    count_delay_day[line[2]] = 1
        except:
            continue

    for key in total_delay_day:
        avg_delay_day[key] = total_delay_day[key]/count_delay_day[key]

    sorted_avg_delay_day = sorted(avg_delay_day, key=avg_delay_day.get, reverse=True)

    print("Average Delay Time by Day of Week:")
    for key in sorted_avg_delay_day:
        print(day_number[key], int(avg_delay_day[key]), 'minutes')
        x_axis.append(day_number[key])
        y_axis.append(int(avg_delay_day[key]))


    #objects = sorted_avg_delay_day
    y_pos = np.arange(len(x_axis))
    #performance = avg_delay_day

    plt.bar(y_pos, y_axis, align='center', alpha=0.5)
    plt.xticks(y_pos, x_axis)
    plt.ylabel('y')
    plt.title('title')

    plt.show()
    print('*Note: Average delay time is calculated with only flights that are delayed.')



############# Function 2: Sort Carrier by Each Delay Reason//For different delay reasons, explore avg delay time for all carriers.
def functionality_2_carrier_rank_delay_reason():
    delay_reason_options = """
Delay Reason Options:
1 - Late Aircraft Delay
2 - Security Delay
3 - NAS Delay
4 - Weather Delay
5 - Carrier Delay
0 - Exit
"""
    while True:
        print(delay_reason_options)
        delay_reason = input("Please enter a number: ")
        try:
            int(delay_reason)
            if int(delay_reason) in range(1, 6, 1):
                delay_reason_column_num = - int(delay_reason)
                sort_carrier_by_delay_reason(delay_reason_column_num, cleaned_table)
            elif int(delay_reason) == 0:
                break
            else:
                print("Invalid Number.")
        except:
            print("Invalid. Please enter a number.")



#################### Mean Function
functionalities = """
*** Main Menu ***
Please choose one to explore:
1 - Carrier Rank by Delay Percentage
2 - Carrier Rank by Delay Reasons
3 - Average Delay Time by Day of Week
4 - Max, Avg, Min delay minutes for a(n) chosen Carrier or Airport
5 - Explore Delay Reasons for a(n) chosen Carrier or Airport
6 - Exit
Your choice:
"""
while True:
    chosen_function = input(functionalities)
    try:
        int(chosen_function)
        if int(chosen_function) == 1:
            functionality_1_carrier_rank_percentage_delay()
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 2:
            functionality_2_carrier_rank_delay_reason()
            # print('Enter "help" for a full list of Carrier Name with Carrier Codes.')
            # print('Enter any key to go back to the *Main Menu*')
            # help_input = input('')
            # if help_input == 'help':
            #     print(carrier_dict)
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 3:
            functionality_3_rank_day()
            print('Enter any key to go back to the *Main menu*')
            input('')
        elif int(chosen_function) == 4:
            functionality_4_basic_stats()
            print('Press "return" to go back to the *Main menu*')
            input('')
        elif int(chosen_function) == 5:
            functionality_5_delay_breakdown()
            print('Press "return" to go back to the *Main menu*')
            input('')
        elif int(chosen_function) == 6:
            print("Goodbye.")
            break
        else:
            print('Invalid Number. Please choose again.')
    except:
        print('Invalid. Please choose again.')