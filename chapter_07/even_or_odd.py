
number = input("Please enter a number and I will tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print("The number you entered is even: " + str(number))
else:
    print("The number you entered is odd: " + str(number))