#name = input("Please enter your name: ")
#print("Hello " + name.title() + "!")

prompt = "\nIf you tell us who you are, we can personalize the message for you"
prompt += "\nEnter 'quit' to end the program: "

active = True

while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)


# print("Hello " + name1 + " we know you are sleepy but you will make it.")
