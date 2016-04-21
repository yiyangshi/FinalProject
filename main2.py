import time
import operator
#from preclean import *
from help import calculate_list
from help import basic_stats
from help import delay_breakdown



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
print(end_time)



############### Basic Stats
while True:
    break ###############################
    basic_stats_input = input("(basic stats)Please select what you like to explore? 1 for carrier, 2 for departure airport")
    try:
        float(basic_stats_input)
        if float(basic_stats_input) == 1:
            basic_stats(1, cleaned_table)
        if float(basic_stats_input) == 2:
            basic_stats(2, cleaned_table)
        else:
            print('Invalid Number')
    except:
        if basic_stats_input == 'exit':
            break
        else:
            print('Please enter a number')



############## Delay Breakdown
while True:
    break ####################
    delay_breakdown_input = input("(delay_breakdown)Please select what you like to explore? 1 for carrier, 2 for departure airport")
    try:
        float(delay_breakdown_input)
        if float(delay_breakdown_input) == 1:
            delay_breakdown(1, cleaned_table)
        if float(delay_breakdown_input) == 2:
            delay_breakdown(2, cleaned_table)
        else:
            print('Invalid Number')
    except:
        if delay_breakdown_input == 'exit':
            break
        else:
            print('Please enter a number')



############# Top 10 Carriers that are most likely to delay


#top_carrier_time = dict()
total_carrier_count = dict()
delay_carrier_count = dict()
for line in cleaned_table[1:]:
    if line[4] in total_carrier_count:
        total_carrier_count[line[4]] += 1
    else:
        total_carrier_count[line[4]] = 1
    try:
        float(line[-6])
        if float(line[-6]) >= 0:
            if line[4] in delay_carrier_count:
                #top_carrier_time[line[4]] += float(line[-6])
                delay_carrier_count[line[4]] += 1
            else:
                #top_carrier_time[line[4]] = float(line[-6])
                delay_carrier_count[line[4]] = 1
    except:
        continue

print(carrier_count)
print(top_carrier_count)

top_carrier = dict()
for key in carrier_count:
    top_carrier[key] = top_carrier_count[key]/carrier_count[key]

#print(top_carrier)
sorted_top_carrier = sorted(top_carrier, key=top_carrier.get, reverse=True)
for key in sorted_top_carrier:
    print(key, top_carrier[key])

#print(sorted_top_carrier)