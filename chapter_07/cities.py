prompt = "\nWhich cities have you visited"
prompt += "\nEnter quit to exit the program: "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(city)