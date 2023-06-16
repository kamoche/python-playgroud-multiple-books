from collections import Counter

vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}

emptyset = set()

letters = set('alice')

# >>> letters.intersection(vowels)
# {'a', 'e', 'i'}

vowels.add('x')
# >>> vowels
# {'i', 'a', 'u', 'o', 'x', 'e'}


# Frozensets are hashable and can
# be used as dictionary keys:
d = {frozenset({1, 2, 3}): 'hello'}
# >>> d[frozenset({1, 2, 3})]
# 'hello'


inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
# >>> inventory
# Counter({'bread': 3, 'sword': 1})
more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
# >>> inventory
# Counter({'bread': 3, 'sword': 2, 'apple': 1})

#>>> Counter(i=4, s=4, p=2, m=1)
#Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
sales = Counter(apple=25, orange=15, banana=12)


# Use a counter
monday_sales = Counter(apple=10, orange=8, banana=3)
sales.update(monday_sales)
#>>> sales
#Counter({'apple': 35, 'orange': 23, 'banana': 15})

# Use a dictionary of counts
tuesday_sales = {"apple": 4, "orange": 7, "tomato": 4}
sales.update(tuesday_sales)
#>>> sales
#Counter({'apple': 39, 'orange': 30, 'banana': 15, 'tomato': 4})
