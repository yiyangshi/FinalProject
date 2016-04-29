# Welcome: Welcome Message at the very beginning of the program
welcome_message = """
*********  WELCOME!  *********
This program explores U.S. flight on-time performance.
You can obtain your own data from U.S. Department of Transportation and run on this program.
To obtain your own data, please check: http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time.
Please also check the available data for data format.

*Note: The program is case sensitive"""



# File Input: Message displayed when user chooses which file to explore
user_file_message = """
Please choose a data file:
1 - Flight Information for January 2016
2 - Flight Information for Febrary 2016
3 - Upload your own file
9 - Get help on downloading your own file
Your choice is:
"""



# File Input: Message to help user download the correct data file from U.S. Department of Transportation Website
download_file_help_message = """
Check http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time to down load your file
*Make sure you select these variables:
YEAR, MONTH, DAY_OF_WEEK, FL_DATE, UNIQUE_CARRIER
ORIGIN, ORIGIN_CITY_NAME, ORIGIN_STATE_NM, DEST, DEST_CITY_NAME
DEST_STATE_NM, CRS_DEP_TIME, DEP_TIME, DEP_DELAY, CRS_ARR_TIME, ARR_TIME
ARR_DELAY, CARRIER_DELAY, WEATHER_DELAY, NAS_DELAY, SECURITY_DELAY
LATE_AIRCRAFT_DELAY
"""



# Main Menu: Functionality Message
main_menu_functionality_message = """
*** Main Menu ***
Please choose one to explore:
1 - Carrier Rank by Delay Percentage (with pics)
2 - Carrier Rank by Average Delay Minutes for a chosen Delay Reasons
3 - Average Delay Minutes by Day of Week (with pics)
4 - Max, Avg, Min delay minutes for a(n) chosen Carrier or Airport
5 - Explore Delay Reasons for a(n) chosen Carrier or Airport
6 - Exit
Your choice:
"""



# Function 2: Delay Reason Options Message
delay_reason_options = """
Delay Reason Options:
1 - Late Aircraft Delay
2 - Security Delay
3 - NAS Delay
4 - Weather Delay
5 - Carrier Delay
0 - Exit
"""



# Function 4: Bais Stats Options Message
basic_stats_options = """
Calculate max, avg, min delay minutes for a:
1 - Carrier
2 - Departure Airport
0 - Exit
"""



# Function 5: Delay Breakdown Options Message
delay_breakdown_options = """
Explore delay reasons for a:
1 - Carrier
2 - Departure Airport
0 - Exit
"""