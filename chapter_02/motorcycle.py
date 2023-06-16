

#modify data in the list
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)

#append element in the list

motorcycles.append('tayota')

print(motorcycles)

print("start from empty list")

motoc = []
motoc.append('honda')
motoc.append('toyota')
motoc.append('mahindra')

print(motoc)

#insert elements
motoc.insert(0,'dream car')

print(motoc)

#deleting an element from the list

del motoc[3]
print(motoc)

#pop an element from a list 

poppedElement = motoc.pop()
print(motoc)
print("Popped moto: " + poppedElement)

#pop element at any position in the list 
print("pop index 0 " + motoc.pop(0))
motoc.append('ducati')
print(motoc)
#remove an element from the list based on its value 
motoc.remove('honda')
print("removing an element " + str(motoc))
#~ print(motoc)




