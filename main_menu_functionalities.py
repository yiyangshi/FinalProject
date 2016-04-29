#import matplotlib
#matplotlib.use('AGG')
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from carrier_dict import *
from messages import *

from help import sort_carrier_by_delay_reason
from help import basic_stats
from help import delay_breakdown



############# Function 1: Carrier Rank by Delay Percentage (with pics)
def functionality_1_carrier_rank_percentage_delay(table):

    #Initialize
    carrier_total_count = dict()
    carrier_delay_count = dict()
    x_axis = []
    y_axis = []

    #loop through each row once. For each carrier, obtain total number of flights and number of delayed flights
    for line in table[1:]: #line 1 are variable names

        #calculate total number of flights
        if line[4] in carrier_total_count: #line[4]: column of carrier code
            carrier_total_count[line[4]] += 1
        else:
            carrier_total_count[line[4]] = 1

        #calculate number of delayed flight
        try:
            float(line[-6]) #line[-6]: arrival delay minutes
            if float(line[-6]) > 0:
                if line[4] in carrier_delay_count:
                    carrier_delay_count[line[4]] += 1
                else:
                    carrier_delay_count[line[4]] = 1
        except:
            continue

    #create dictionary with key = carrier code, value = sample delay percentage
    top_carrier = dict()
    for key in carrier_total_count:
        top_carrier[key] = carrier_delay_count[key]/carrier_total_count[key]

    #sort top_carrier by key
    sorted_top_carrier = sorted(top_carrier, key=top_carrier.get, reverse=True)

    #print by ranking sequence
    print("Carriers Delay Probability: ")
    rank = 1
    for key in sorted_top_carrier:
        print("No.", rank, "  ", int((top_carrier[key])*100), "%","  ", carrier_dict[key])
        rank +=1
        x_axis.append(key)
        y_axis.append(int((top_carrier[key])*100))

    #graph visualization
    y_pos = np.arange(len(x_axis))
    plt.bar(y_pos, y_axis, align='center', alpha=0.5)
    plt.xticks(y_pos, x_axis)
    plt.ylabel('Percentage(%)')
    plt.title('Carrier Delay Probability')
    plt.show()



############# Function 2: Carrier Rank by Average Delay Minutes for a chosen Delay Reasons
def functionality_2_carrier_rank_delay_reason(table):
    while True:
        print(delay_reason_options)
        delay_reason = input("Please enter a number: ")
        try:
            int(delay_reason)
            if int(delay_reason) in range(1, 6, 1): #line[-1] to line[-5]: delay minutes for each of the 5 delay reason
                delay_reason_column_num = - int(delay_reason)
                sort_carrier_by_delay_reason(delay_reason_column_num, table)
            elif int(delay_reason) == 0:
                break
            else:
                print("Invalid Number.")
        except:
            print("Invalid. Please enter a number.")



################### Function 3: Avg delay minutes for different day of week
def functionality_3_rank_day(table):

    #Initialize
    day_total_delay_minutes = dict()
    day_delay_count = dict()
    day_avg_delay_minutes = dict()
    day_number = {'1': 'Mon: ', '2': 'Tue: ', '3': 'Wed: ', '4': 'Thu: ', '5': 'Fri: ', '6': 'Sat: ', '7': 'Sun: '}
    x_axis = []
    y_axis = []

    #loop through each row once. For each day, obtain total delay minutes and number of delayed flights
    for line in table[1:]:
        try:
            float(line[-6]) #line[-6]: arrival delay minutes
            if float(line[-6]) > 0:
                if line[2] in day_total_delay_minutes: #line[2]: day of week
                    day_total_delay_minutes[line[2]] += float(line[-6])
                    day_delay_count[line[2]] += 1
                else:
                    day_total_delay_minutes[line[2]] = float(line[-6])
                    day_delay_count[line[2]] = 1
        except:
            continue

    #calculate average delay minutes for each day of week
    for key in day_total_delay_minutes:
        day_avg_delay_minutes[key] = day_total_delay_minutes[key]/day_delay_count[key]

    #sort day_avg_delay_minutes by key
    sorted_day_avg_delay_minutes = sorted(day_avg_delay_minutes, key=day_avg_delay_minutes.get, reverse=True)

    #print by ranking sequence
    print("Average Delay Minutes by Day of Week:")
    for key in sorted_day_avg_delay_minutes:
        print(day_number[key], int(day_avg_delay_minutes[key]), 'minutes')
        x_axis.append(day_number[key])
        y_axis.append(int(day_avg_delay_minutes[key]))

    #graph visualization
    y_pos = np.arange(len(x_axis))
    plt.bar(y_pos, y_axis, align='center', alpha=0.5)
    plt.xticks(y_pos, x_axis)
    plt.ylabel('Minutes')
    plt.title('Average Delay Time by Day of Week')
    plt.show()

    #note
    print('*Note: Average delay time is calculated with only flights that are delayed.')



############### Function 4: Basic Stats
def functionality_4_basic_stats(table):
    while True:
        print(basic_stats_options)
        basic_stats_input = input("Please enter a number: ")
        try:
            float(basic_stats_input)
            if float(basic_stats_input) == 1: #1 - carrier
                basic_stats(1, table)
            elif float(basic_stats_input) == 2: #2 - airport
                basic_stats(2, table)
            elif float(basic_stats_input) == 0: #0 - exit
                break
            else:
                print('Invalid Number. Please try again.')
        except:
             print('Invalid. Please enter a number.')



############# Function 5: Delay Breakdown
def functionality_5_delay_breakdown(table):
    while True:
        print(delay_breakdown_options)
        delay_breakdown_input = input("Please enter a number: ")
        try:
            float(delay_breakdown_input)
            if float(delay_breakdown_input) == 1: #1 - carrier
                delay_breakdown(1, table)
            elif float(delay_breakdown_input) == 2: #2 - airport
                delay_breakdown(2, table)
            elif float(delay_breakdown_input) == 0: #0 - exit
                break
            else:
                print('Invalid Number. Please try again.')
        except:
            print('Invalid. Please enter a number.')