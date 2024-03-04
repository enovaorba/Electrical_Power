from Fanc import Fanc
from datetime import datetime, timedelta

# Define the start and end timestamps
start = datetime.strptime("2023-11-06:00:00", "%Y-%m-%d:%H:%M")
end = datetime.strptime("2024-01-19:00:00", "%Y-%m-%d:%H:%M")

# Define the time interval for each iteration (e.g., 1 day)
interval = timedelta(days=1)

# Run the loop
current_time = start
while current_time < end:
    # Start of the current day
    current_day_start = datetime(current_time.year, current_time.month, current_time.day, 0, 0)
    
    # End of the current day
    current_day_end = current_day_start + interval
    
    # Run the query for the current day
    Fanc.Get_LP("S540321494", current_day_start.strftime("%Y-%m-%dT%H:%M:%S"), current_day_end.strftime("%Y-%m-%dT%H:%M:%S"))
    
    # Move to the next day
    current_time += interval
