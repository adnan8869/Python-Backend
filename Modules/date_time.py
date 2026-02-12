from datetime import datetime, timedelta
from time import strftime

# current date and time
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S")) 
# date and time after 5 days
future_date = now + timedelta(days=5)
print("Date and time after 5 days:", future_date.strftime("%Y-%m-%d %H:%M:%S"))