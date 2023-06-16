file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love python \n")
    file_object.write("It's great for scripting \n")

with open(file_name, 'a') as file_object:
    file_object.write("It can also create great games")