from datetime import datetime
import pytz

# Get current UTC datetime
utc_now = datetime.utcnow()

# Set the time zone to Israel time
israel_timezone = pytz.timezone('Asia/Jerusalem')
israel_now = utc_now.replace(tzinfo=pytz.utc).astimezone(israel_timezone)

print("UTC Time:", utc_now)
print("Israel Time:", israel_now)