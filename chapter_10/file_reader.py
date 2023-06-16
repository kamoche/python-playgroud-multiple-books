file_name = 'pi_digits.txt'
try:
    with open(file_name) as file_object:
        contents = file_object.read()
        print(contents.rstrip())

    with open(file_name) as file_object:
        for line in file_object:
            print('Line: ' + line.rstrip())

    with open(file_name) as file_object:
        lines = file_object.readlines()

    pi_string=''
    for line in lines:

        pi_string += line.rstrip()

    print(pi_string)
    print(len(pi_string))

except FileNotFoundError:
    msg = "Sorry, file " + file_name + " not found."
    print(msg)
