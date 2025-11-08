
import pytz
from datetime import datetime

# Get the local timezone (example: 'Asia/Kolkata', 'America/New_York', etc.)
local_tz = pytz.timezone('Asia/Ho_Chi_Minh')  # Change this to your local timezone

# Get current time in that timezone
local_time = datetime.now(local_tz)
local_time_date_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
local_time_date = local_time.strftime('%Y-%m-%d')

def unixTimestamp():
  # return '%s |> ' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  return '🔥 %s |> ' % local_time_date_time
