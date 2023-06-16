from name_function import get_formatted_name

while True:
    first_name = input("Please enter first name: ")
    if first_name == 'quit' or first_name == 'q':
        break
    last_name = input("Enter last name: ")
    if last_name == 'quit' or last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name,last_name)
    print("\nFormatted name is: " + formatted_name)