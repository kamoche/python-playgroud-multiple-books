print("Enter two numbers and I'll divide them")
print("Enter 'q' to quit")
while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You don't divide by 0!")
    else:
        print("The answer is: "+ str(answer))

