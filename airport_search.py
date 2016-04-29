import re

def airport_search():

    going = True
    while going:

        #Initialize
        user_regex = input('Please enter a location: ')
        result = 0
        airport_table = open('airport_table.txt')

        #Print search result
        for line in airport_table:
            if re.findall(user_regex,line):
                print(line[1:4], ':', line[7:-1])
                result += 1
        if result == 0:
            print('No result for such location.')
        else:
            pass

        #Input Control
        while True:
            user_input = input('Enter 0 to Exit. Enter 1 to search again: ')
            try:
                float(user_input)
                if float(user_input) == 0:
                    going = False
                    break
                elif float(user_input) == 1:
                    break
                else:
                    print('Invalid Number. Please try again.')
            except:
                print('Invalid. Please enter a number.')
