from carrier_dict import carrier_dict
from airport_dict import *

########### calculate unique values of a column
def calculate_list(column_num, table):
    newlist = []
    for line in table[1:]:
        if line[column_num] not in newlist:
            newlist.append(line[column_num])
    return(newlist)



############# take carrier/airport name as input and calculate the max, mean, and min delay time for the carrier
def basic_stats(attribute, table):
    while True:
        if attribute == 1:
            attribute_basic_stats = input('Please enter a carrier code (Enter "help" for complete carrier code list): ')
            column = 4
        if attribute == 2:
            attribute_basic_stats = input('Please enter an airport code (Enter "help" to search for airport code): ')
            column = 5
        if attribute_basic_stats != "help":
            attribute_max = 0
            attribute_avg = 0
            attribute_min = 10000
            attribute_total = 0
            attribute_count = 0
            for line in table:
                if line[column] == attribute_basic_stats:
                    try:
                        float(line[-6])
                        if float(line[-6]) > 0:
                            attribute_count += 1
                            attribute_total += float(line[-6])
                            if float(line[-6]) >= attribute_max:
                                attribute_max = float(line[-6])
                            if float(line[-6]) <= attribute_min:
                                attribute_min = float(line[-6])
                    except:
                        continue
            try:
                attribute_avg = attribute_total/attribute_count
                print('Max Delay Minutes: ', int(attribute_max))
                print('Avg Delay Minutes: ', int(attribute_avg))
                print('Min Delay Minutes: ', int(attribute_min))
                print('Press "return" to go back.')
                input('')
                break
            except:
                print('Invalid code. Please try again.')
        else:
            attribute_code_list = calculate_list(column, table)
            if len(attribute_code_list) == 12:
                for element in attribute_code_list:
                    print(element, ":   ", carrier_dict[element])
            else:
                airport_search()



############# take carrier/airport name as input and calculate the top delay reasons and corresponding delay time for the carrier.
delay = {'CARRIER_DELAY': 'Carrier Delay: ', 'NAS_DELAY': 'NAS Delay: ', 'LATE_AIRCRAFT_DELAY': 'Late Aircraft Delay: ', 'WEATHER_DELAY': 'Weather Delay: ', 'SECURITY_DELAY': 'Security Delay: '}
def delay_breakdown(attribute, table):
    while True:
        if attribute == 1:
            attribute_delay_breakdown = input('Please enter a carrier code (Enter "help" for carrier code list): ')
            column = 4
            attribute_code_list = calculate_list(column, table)
        if attribute == 2:
            attribute_delay_breakdown = input('Please enter an airport code (Enter "help" to search for airport code): ')
            column = 5
            attribute_code_list = calculate_list(column, table)
        if attribute_delay_breakdown in attribute_code_list:
            attribute_delay_total = dict()
            attribute_delay_count = dict()
            total_delay_count = 0
            for column_num in range(-5, 0):
                attribute_delay_total[table[0][column_num]] = 0
                attribute_delay_count[table[0][column_num]] = 0
            for line in table:
                if line[column] == attribute_delay_breakdown:
                    try:
                        float(line[-6])
                        if float(line[-6]) > 0:
                            total_delay_count += 1
                    except:
                        pass
                    for column_num in range(-5, 0):
                        try:
                            float(line[column_num])
                            if float(line[column_num]) > 0:
                                attribute_delay_total[table[0][column_num]] += float(line[column_num])
                                attribute_delay_count[table[0][column_num]] += 1
                        except:
                            pass

            attribute_delay_percentage = dict()
            for key in attribute_delay_count:
                attribute_delay_percentage[key] = attribute_delay_count[key]/total_delay_count

            sorted_attribute_delay_percentage = sorted(attribute_delay_percentage, key = attribute_delay_percentage.get, reverse = True)

            print("Percentage of delay caused by each delay reason: ")
            for key in sorted_attribute_delay_percentage:
                print(delay[key], int(attribute_delay_percentage[key]*100), '%')
            print('*Note: The percentages may not add up to 100% because a delay can be caused by multiple reasons.')
            print('')

            attribute_delay_avg = dict()
            for key in attribute_delay_total:
                if attribute_delay_count[key] > 0:
                    attribute_delay_avg[key] = attribute_delay_total[key]/attribute_delay_count[key]
                else:
                    attribute_delay_avg[key] = 0

            sorted_attribute_delay_avg = sorted(attribute_delay_avg, key=attribute_delay_avg.get, reverse=True)

            print("Average delay time for each delay reason: ")
            for key in sorted_attribute_delay_avg:
                print('Avg', delay[key], int(attribute_delay_avg[key]), 'minutes')
            print('*Note: Average delay time is calculated with only flights that are delayed.')
            print('Press "return" to go back.')
            input('')
            break

        elif attribute_delay_breakdown == 'help':
            attribute_code_list = calculate_list(column, table)
            if len(attribute_code_list) == 12:
                for element in attribute_code_list:
                    print(element, ":   ", carrier_dict[element])
            else:
                airport_search()

        else:
            print('Invalid code. Please try again.')



############# Sort Carrier by Each Delay Reason
def sort_carrier_by_delay_reason(column, table):
    total = dict()
    count = dict()
    for line in table[1:]:
        try:
            float(line[column])
            if float(line[column]) > 0:
                if line[4] in total:
                    total[line[4]] += float(line[column])
                    count[line[4]] += 1
                else:
                    total[line[4]] = float(line[column])
                    count[line[4]] = 1
        except:
            continue

    carrier_by_delay_reason = dict()
    for key in total:
        carrier_by_delay_reason[key] = total[key]/count[key]

    sorted_carrier_by_delay_reason = sorted(carrier_by_delay_reason, key=carrier_by_delay_reason.get, reverse=True)

    print("Sorted Carrier by Delay Reason:")
    rank = 1
    for key in sorted_carrier_by_delay_reason:
        print('No.', rank, '    ', int(carrier_by_delay_reason[key]), 'minutes', '   ', carrier_dict[key])
        rank +=1
    input('Enter any key to go back.')
