
while True:
    age = input("To get your ticket cost, please enter your age\nEnter 'quit' to exit the program:  ")
    if age != "quit":
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif age < 12:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15")
    else:
        break
