import json

file_name = 'numbers.json'

try:
    with open(file_name) as f_obj:
       numbers = json.load(f_obj)
except FileNotFoundError:
    pass
else:
    print(numbers)