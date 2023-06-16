import json

numbers = [x for x in range(1,20)]

file_name = "numbers.json"

with open(file_name,'w') as f_obj:
    json.dump(numbers,f_obj)

