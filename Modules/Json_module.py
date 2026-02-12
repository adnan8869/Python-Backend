import json
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
# Convert JSON string to Python dictionary
dict_data = json.loads(json_string)
print(dict_data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Convert Python dictionary to JSON string
json_again = json.dumps(dict_data)
print(json_again)  # {"name": "Alice", "age": 30, "city": "New York"}