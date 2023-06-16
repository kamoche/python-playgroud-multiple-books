
request_toppings = ['pepperoni']

if request_toppings:
    for topping in request_toppings:
        print("Adding " +topping + ".")
    print("\nFinished making pizza\n")

else:
    print("Are you sure you want to order a plain pizza")


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, " + requested_topping + " is not available at the moment.")
print("\nFinished making you pizza")
