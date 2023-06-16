def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

genexpr = (x * x for x in range(3))

dict_vec = {'y': 0, 'z': 1, 'x': 1}

print_vector(*tuple_vec)
print_vector(*list_vec)
print_vector(*genexpr)
print_vector(**dict_vec)