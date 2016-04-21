#from main2 import cleaned_table



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
            attribute_basic_stats = input('Please enter a carrier code (Enter "help" for carrier code list): ')
            column = 4
        if attribute == 2:
            attribute_basic_stats = input('Please enter an airport code (Enter "help" for airport code list): ')
            column = 5
        if attribute_basic_stats != "help":
            print("valid")
            attribute_max = 0
            attribute_mean = 0
            attribute_min = 10000
            attribute_total = 0
            attribute_count = 0
            print("a")
            for line in table:
                if line[column] == attribute_basic_stats:
                    attribute_count += 1
                    if float(line[-6]) >= 0:
                        attribute_total += float(line[-6])
                        if float(line[-6]) >= attribute_max:
                            attribute_max = float(line[-6])
                        if float(line[-6]) <= attribute_min:
                            attribute_min = float(line[-6])
            print(attribute_max)
            try:
                attribute_mean = attribute_total/attribute_count
                print('Max Delay Minutes: ', "%.2f" % attribute_max)
                print('Mean Delay Minutes: ', "%.2f" % attribute_mean)
                print('Min Delay Minutes: ', "%.2f" % attribute_min)
                break
            except:
                print('Invalid code. Please try again.')
        else:
            attribute_code_list = calculate_list(column, table)
            print(attribute_code_list)



############# take carrier name as input and calculate the top delay reasons and corresponding delay time for the carrier.
def delay_breakdown(attribute, table):
    while True:
        if attribute == 1:
            attribute_delay_breakdown = input('Please enter a carrier code (Enter "help" for carrier code list): ')
            column = 4
            attribute_code_list = calculate_list(column, table)
        if attribute == 2:
            attribute_delay_breakdown = input('Please enter an airport code (Enter "help" for airport code list): ')
            column = 5
            attribute_code_list = calculate_list(column, table)
        if attribute_delay_breakdown in attribute_code_list:
            attribute_delay_reason = dict()
            attribute_delay_reason['Carrier Delay: '] = 0
            attribute_delay_reason['Weather Delay: '] = 0
            attribute_delay_reason['NAS Delay: '] = 0
            attribute_delay_reason['Security Delay: '] = 0
            attribute_delay_reason['Late Aircraft Delay: '] = 0

            for line in table:
                if line[column] == attribute_delay_breakdown:
                    if line[-5] != '':
                        attribute_delay_reason['Carrier Delay: '] += float(line[-5])
                    if line[-4] != '':
                        attribute_delay_reason['Weather Delay: '] += float(line[-4])
                    if line[-3] != '':
                        attribute_delay_reason['NAS Delay: '] += float(line[-3])
                    if line[-2] != '':
                        attribute_delay_reason['Security Delay: '] += float(line[-2])
                    if line[-1] != '':
                        attribute_delay_reason['Late Aircraft Delay: '] += float(line[-1])

            sorted_attribute_delay_reason = sorted(attribute_delay_reason, key=attribute_delay_reason.get, reverse=True)

            for key in sorted_attribute_delay_reason:
                print(key, attribute_delay_reason[key])

            break

        elif attribute_delay_breakdown == 'help':
            print(attribute_code_list)

        else:
            print('Invalid code. Please try again.')

