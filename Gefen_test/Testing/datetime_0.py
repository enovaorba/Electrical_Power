from datetime import datetime
import pytz

# Define Israel timezone
israel_timezone = pytz.timezone('Asia/Jerusalem')

# Format datetime as per the specified format
formatted_datetime_israel = datetime.now(israel_timezone).strftime('%Y-%m-%dT%H:%M:%S')

# Print the formatted datetime
print(formatted_datetime_israel)