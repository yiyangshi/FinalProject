from carrier_dict import *
from airport_search import *



# Functionality 2 Helper: sort_carrier_by_delay_reason(column, table)
# Sort Carrier by Average Delay Minutes for a chosen Delay Reasons
def sort_carrier_by_delay_reason(column, table):

    #Initialize
    total_delay_minutes = dict()
    count_delay_times = dict()

    #loop through each row once. For the chosen delay reason, obtain total delay minutes and number of delayed flights
    for line in table[1:]: #line 1 are variable names
        try:
            float(line[column]) #line[column]: delay mintutes for delay reason [column]
            if float(line[column]) > 0:
                if line[4] in total_delay_minutes: #line[4]: carrier code
                    total_delay_minutes[line[4]] += float(line[column])
                    count_delay_times[line[4]] += 1
                else:
                    total_delay_minutes[line[4]] = float(line[column])
                    count_delay_times[line[4]] = 1
        except:
            continue

    #calculate average delay minutes for the chosen delay reason
    avg_delay_minutes = dict()
    for key in total_delay_minutes:
        avg_delay_minutes[key] = total_delay_minutes[key]/count_delay_times[key]

    #sort avg_delay_minutes by key
    sorted_avg_delay_minutes = sorted(avg_delay_minutes, key=avg_delay_minutes.get, reverse=True)

    #print by ranking sequence
    print("Sorted Carrier by Delay Reason:")
    rank = 1
    for key in sorted_avg_delay_minutes:
        print('No.', rank, '    ', int(avg_delay_minutes[key]), 'minutes', '   ', carrier_dict[key])
        rank +=1
    input('Enter any key to go back.')



# Functionality 4/5 Helper's Helper: calculate_list(column_num, table)
# calculate unique values of a column
def calculate_list(column_num, table):
    newlist = []
    for line in table[1:]:
        if line[column_num] not in newlist:
            newlist.append(line[column_num])
    return(newlist)



# Functionality 4 Helper: basic_stats(option, table)
# take carrier/airport name as input and calculate the max, mean, and min delay time
def basic_stats(option, table):

    while True:

        #user select option carrier or option airport.
        if option == 1: #1 - carrier
            option_input = input('Please enter a carrier code (Enter "help" for complete carrier code list): ')
            column = 4 #line[4]: carrier code
        if option == 2: #2 - airport
            option_input = input('Please enter an airport code (Enter "help" to search for airport code): ')
            column = 5 #line[5]: airport code

        # calculate max, avg, min for user input
        if option_input != "help":

            #Initialize
            input_max = 0
            input_min = 10000
            input_total = 0
            input_count = 0

            #loop through each row once. Obtain max, min, total, counts
            for line in table:
                if line[column] == option_input:
                    try:
                        float(line[-6]) #line[-6]: arrival delay minutes
                        if float(line[-6]) > 0:

                            #calculate counts
                            input_count += 1

                            #calculate total delay minutes
                            input_total += float(line[-6])

                            #calculate max
                            if float(line[-6]) >= input_max:
                                input_max = float(line[-6])

                            #calculate min
                            if float(line[-6]) <= input_min:
                                input_min = float(line[-6])

                    except:
                        continue

            #print
            try: #varify if input_count = 0
                input_avg = input_total/input_count
                print('Max Delay Minutes: ', int(input_max))
                print('Avg Delay Minutes: ', int(input_avg))
                print('Min Delay Minutes: ', int(input_min))
                print('Enter any key to go back.')
                input('')
                break
            except:
                print('Invalid code. Please try again.')

        #Initiate "help" functions for carrier/airport
        else:

            #calculate number of unique codes for carrier/airport
            option_code_list = calculate_list(column, table)

            #carrier code help
            if len(option_code_list) == 12:
                for element in option_code_list:
                    print(element, ":   ", carrier_dict[element])

            #airport code help
            else:
                airport_search()



# Functionality 5 Helper: delay_breakdown(attribute, table)
# take carrier/airport name as input and calculate the top delay reasons and corresponding delay time for the carrier.

delay = {'CARRIER_DELAY': 'Carrier Delay: ', 'NAS_DELAY': 'NAS Delay: ', 'LATE_AIRCRAFT_DELAY': 'Late Aircraft Delay: ', 'WEATHER_DELAY': 'Weather Delay: ', 'SECURITY_DELAY': 'Security Delay: '}

def delay_breakdown(delay_reason_option, table):
    while True:

        # user select option carrier or option airport.
        if delay_reason_option == 1: #1 - carrier
            delay_reason_input = input('Please enter a carrier code (Enter "help" for carrier code list): ')
            column = 4 #line[4]: carrier code
            option_code_list = calculate_list(column, table)
        if delay_reason_option == 2: #2 - airport
            delay_reason_input = input('Please enter an airport code (Enter "help" to search for airport code): ')
            column = 5 #line[5]: airport code
            option_code_list = calculate_list(column, table)

        #calculate total delay minutes for each delay reason, total number of delay for each delay reason, and total number of delay
        if delay_reason_input in option_code_list:

            #Initialize
            input_delay_minutes_by_delay_reason = dict()
            input_delay_count_by_delay_reason = dict()
            input_total_delay_count = 0
            for column_num in range(-5, 0): #the five delay reasons
                input_delay_minutes_by_delay_reason[table[0][column_num]] = 0
                input_delay_count_by_delay_reason[table[0][column_num]] = 0

            #calculate total delay minutes for each delay reason, total number of delay for each delay reason, and total number of delay
            for line in table:
                if line[column] == delay_reason_input:

                    #count total number of delay
                    try:
                        float(line[-6])
                        if float(line[-6]) > 0:
                            input_total_delay_count += 1
                    except:
                        pass

                    #for each delay reason, calculate total delay minutes and total number of delay
                    for column_num in range(-5, 0):
                        try:
                            float(line[column_num])
                            if float(line[column_num]) > 0:

                                #calculate total delay minutes
                                input_delay_minutes_by_delay_reason[table[0][column_num]] += float(line[column_num])

                                #calculate total number of delay
                                input_delay_count_by_delay_reason[table[0][column_num]] += 1
                        except:
                            pass

            #calculate percentage delay caused by each delay reason
            input_delay_percentage_by_delay_reason = dict()
            for key in input_delay_count_by_delay_reason:
                if input_total_delay_count > 0:
                    input_delay_percentage_by_delay_reason[key] = input_delay_count_by_delay_reason[key]/input_total_delay_count
                else:
                    input_delay_percentage_by_delay_reason[key] = 0

            #sort input_delay_percentage_by_delay_reason
            sorted_input_delay_percentage_by_delay_reason = sorted(input_delay_percentage_by_delay_reason, key = input_delay_percentage_by_delay_reason.get, reverse = True)

            #print percentages by ranking sequence
            print("Percentage of delay caused by each delay reason: ")
            for key in sorted_input_delay_percentage_by_delay_reason:
                print(delay[key], int(input_delay_percentage_by_delay_reason[key]*100), '%')
            print('*Note: The percentages may not add up to 100% because a delay can be caused by multiple or unlisted reasons.')
            print('')


            #calculate average delay minutes caused by each delay reason
            input_avg_delay_minutes_by_delay_reason = dict()
            for key in input_delay_minutes_by_delay_reason:
                if input_delay_count_by_delay_reason[key] > 0:
                    input_avg_delay_minutes_by_delay_reason[key] = input_delay_minutes_by_delay_reason[key]/input_delay_count_by_delay_reason[key]
                else:
                    input_avg_delay_minutes_by_delay_reason[key] = 0

            #sort input_avg_delay_minutes_by_delay_reason
            sorted_input_avg_delay_minutes_by_delay_reason = sorted(input_avg_delay_minutes_by_delay_reason, key=input_avg_delay_minutes_by_delay_reason.get, reverse=True)

            #print average minutes by ranking sequence
            print("Average delay minutes for each delay reason: ")
            for key in sorted_input_avg_delay_minutes_by_delay_reason:
                print('Avg', delay[key], int(input_avg_delay_minutes_by_delay_reason[key]), 'minutes')
            print('*Note: Average delay time is calculated with only flights that are delayed.')

            #return to main menu
            input('Enter any key to go back to the *Main Menu*')
            break

        # Initiate "help" functions for carrier/airport
        elif delay_reason_input == 'help':

            #calculate number of unique codes for carrier/airport
            option_code_list = calculate_list(column, table)

            #carrier code help
            if len(option_code_list) == 12:
                for element in option_code_list:
                    print(element, ":   ", carrier_dict[element])

            #airport code help
            else:
                airport_search()

        else:
            print('Invalid code. Please try again.')



