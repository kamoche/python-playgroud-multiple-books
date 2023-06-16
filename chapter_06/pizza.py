#Store pizza ordered by customer

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

#Summarize the order
print("You ordered a " + pizza['crust'] + "_crust with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping.title())