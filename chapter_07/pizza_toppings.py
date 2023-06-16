
pizza_size = ['small', 'medium', 'large']
pizza_crust = ['thin', 'thick']
pizza_toppings = ['mushroom','pepperoni','extra cheese']


available_pizza_type = { 'crust': pizza_crust, 'size': pizza_size , 'toppings': pizza_toppings}
requested_toppings = []
topping_prompt = "\nPlease select pizza topping you would like to be on your pizza"
topping_prompt += "\nEnter enter'quit' to exit program: "

while True:
    topping = input(topping_prompt)
    if topping != "quit":
        if topping in available_pizza_type['toppings']:
            if topping in requested_toppings:
                print(topping.title() + " is already in your selected toppingskk.")
            else:
                print("You have selected: " + topping)
                requested_toppings.append(topping)
                if requested_toppings:
                    print("Your current toppings are as follow: " + str(requested_toppings))

        else:
            print(topping.title() + " is not available at the moment")

    else:
        if requested_toppings:
            print("You can now have a sit, your pizza will take at least 5 min")
            break
        else:
            print("Exiting the program")
            break