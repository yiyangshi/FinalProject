import time
from main_menu_functionalities import *


# Initialize the program. Import File. Save the file as "lines".
print(welcome_message)
while True:
    user_file_input = input(user_file_message)
    try:
        float(user_file_input)
        if float(user_file_input) == 1:
            with open('Jan.csv') as f:
                lines = f.readlines()
            break
        elif float(user_file_input) == 2:
            with open('Feb.csv') as f:
                lines = f.readlines()
            break
        elif float(user_file_input) == 3:
            user_uploaded_file = input("Please enter the file name: ")
            try:
                with open(user_uploaded_file) as f:
                    lines = f.readlines()
                break
            except:
                print("Invalid File Name. Please try again.")
                continue
        elif float(user_file_input) == 9:
            print(download_file_help_message)
            continue
        else:
            print("Invalid Number. Please try again.")
    except:
        print("Invalid. Please try again.")



# Clean Up Table
print("Please wait while the file is being cleaned...")
start_time = time.time() # Count the time used to clean up the file. The cleaning on average takes 17 seconds.

#create table from the saved file "lines".
table = []
for line in lines:
    line = line.strip()
    line = line.split(',')
    del line[-1]
    table.append(line)

#clean each line in table and form a cleaned table
cleaned_table = [[] for x in range(len(table))]
cleaned_line = []
i = 0
for line in table:
    for element in line:
        element = element.strip()
        while element.startswith('"'): #when reading the csv file, quotes were added to string variable as part of the string
            element = element[1:]
        while element.endswith('"'):
            element = element[:-1]
        element = element.strip()
        cleaned_line.append(element)
    cleaned_table[i] = cleaned_line
    cleaned_line = []
    i += 1

end_time=time.time()-start_time # Time count end.
print("Your file is loaded. It took", int(end_time),"seconds to clean your file." )



# Mean Function
while True:
    chosen_function = input(main_menu_functionality_message)
    try:
        int(chosen_function)
        if int(chosen_function) == 1:
            functionality_1_carrier_rank_percentage_delay(cleaned_table)
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 2:
            functionality_2_carrier_rank_delay_reason(cleaned_table)
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 3:
            functionality_3_rank_day(cleaned_table)
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 4:
            functionality_4_basic_stats(cleaned_table)
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 5:
            functionality_5_delay_breakdown(cleaned_table)
            input('Enter any key to go back to the *Main Menu*')
        elif int(chosen_function) == 6:
            print("Goodbye.")
            break
        else:
            print('Invalid Number. Please choose again.')
    except:
        print('Invalid. Please choose again.')