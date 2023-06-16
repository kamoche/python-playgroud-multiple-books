age = 4

if age < 4:
    price = 0
elif age < 18:
    price = 8
elif age < 25:
    price = 9
else:
    price = 10

print("Your admission cost is: $" + str(price) + ".")
