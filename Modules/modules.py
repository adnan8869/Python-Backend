from datetime import datetime, timedelta
from time import strftime

# current date and time
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S")) 
# date and time after 5 days
future_date = now + timedelta(days=5)
print("Date and time after 5 days:", future_date.strftime("%Y-%m-%d %H:%M:%S"))




import json
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
# Convert JSON string to Python dictionary
dict_data = json.loads(json_string)
print(dict_data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Convert Python dictionary to JSON string
json_again = json.dumps(dict_data)
print(json_again)  # {"name": "Alice", "age": 30, "city": "New York"}