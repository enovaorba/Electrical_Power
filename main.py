import os
from Fanc import Fanc
from Fanc_Get_Data import Fanc_Get_Data
#from FancSftp import FancSftp
from datetime import datetime, timedelta
#import pytz
from FancOutputFiles import FancOutputFiles

## Define Israel timezone
#israel_timezone = pytz.timezone('Asia/Jerusalem')
#Fanc_Get_Data.run_stored_procedure_with_parameters("run_counters", ("2024-02-26 00:00:00", "2024-02-27 00:00:00"))
directory = os.getcwd()
f=open(directory + "/Last_Date_LP.txt", "r")
S_Last_Date_LP = f.read()
#date_object = datetime.datetime.strptime(startOfIntervalFrom, '%Y-%m-%dT%H:%M:%S')
lp_datetime = datetime.strptime(S_Last_Date_LP, '%Y-%m-%dT%H:%M:%S')
lp_plus_48_hours = lp_datetime + timedelta(hours=48)
# Check if lp_plus_48_hours is greater than the current datetime
#if lp_plus_48_hours < datetime.now():
#   print("Start raning script.")
#else:
#   print("Less than 48 hours have passed. Exiting.")
#   exit()
#Fanc_Get_Data.sql_run_script("SELECT * FROM Gefen_LP_counters_30_minutes_Consdomestic LIMIT 50")

Fanc.PrintFile(" *** Start App ***" ,"/EventFile.ini")

start = lp_datetime
current_datetime = datetime.now()
two_days_ago = current_datetime - timedelta(days=2)
end = two_days_ago.replace(hour=0, minute=0, second=0, microsecond=0)


#start = datetime.strptime("2023-11-06:00:00", "%Y-%m-%d:%H:%M")
#end = datetime.strptime("2024-01-19:00:00", "%Y-%m-%d:%H:%M")

# Define the time interval for each iteration (e.g., 1 day)
interval = timedelta(days=1)
Count_days=0
# Run the loop
current_time = start


while current_time < end:
    # Start of the current day
    current_day_start = datetime(current_time.year, current_time.month, current_time.day, 0, 0)
    
    # End of the current day
    current_day_end = current_day_start + interval
    
    # Run the query for the current day
    Fanc.Get_LP("S540321494", current_day_start.strftime("%Y-%m-%dT%H:%M:%S"), current_day_end.strftime("%Y-%m-%dT%H:%M:%S"))
    
    startOfIntervalTo = current_day_end.strftime('%Y-%m-%dT%H:%M:%S')
    with open(directory + "/Last_Date_LP.txt", "w") as file:
        file.write(startOfIntervalTo)
    Fanc.PrintFile("Insert Data current_time-" + current_day_end.strftime("%Y-%m-%dT%H:%M:%S"),"/EventFile.ini")
    
    #Fanc_Get_Data.sql_run_script("CALL run_counters('" + current_day_start.strftime("%Y-%m-%dT%H:%M:%S") + "','"+ current_day_end.strftime("%Y-%m-%dT%H:%M:%S") + "');")
    Fanc_Get_Data.run_stored_procedure_with_parameters("run_counters", (current_day_start.strftime("%Y-%m-%dT%H:%M:%S"), current_day_end.strftime("%Y-%m-%dT%H:%M:%S")))
    Fanc.PrintFile("CALL run_counters('" + current_day_start.strftime("%Y-%m-%dT%H:%M:%S") + "','"+ current_day_end.strftime("%Y-%m-%dT%H:%M:%S") + "')","/EventFileApp.ini")            
    # Move to the next day
    current_time += interval   
    Count_days = Count_days + 1
# updete Last_Date_LP.txt file
#startOfIntervalTo = end.strftime('%Y-%m-%dT%H:%M:%S')
#if Count_days > 0 :
#    with open(directory + "/Last_Date_LP.txt", "w") as file:
#        file.write(startOfIntervalTo)

xml_file_name=FancOutputFiles.create_feport_files()


Fanc.PrintFile("Count_days-" + str(Count_days) + " Insert O.K","/EventFileApp.ini")
# send to NOGA
#xml_file_name = ""
#if (xml_file_name != ""):
#    FancSftp.sftp_upload('/home/avi/scripts_python/Gefen/gefenssh.key','le3srqnJ','nofrn#inova','snoga.noga-iso.co.il', FancOutputFiles.directory + "/send_report_xml/" + xml_file_name ,'/External Users BeforeScan/' + xml_file_name)
Fanc.PrintFile(" *** End App ***" ,"/EventFile.ini")
Fanc.PrintFile(" *** End App ***" ,"/EventFileApp.ini")
print("*** End raning script ***")