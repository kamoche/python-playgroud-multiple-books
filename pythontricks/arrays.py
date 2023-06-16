arr = ['one', 'two', 'three']

arr[1] = 'hello'
del arr[1]
arr.append(23)

arr1 = 'one', 'two', 'three'

arr += (23,)


import array

arr2 = array.array('f', (1.0, 1.5, 2.0, 2.5))


arr2[1] = 23.0

del arr2[1]

arr2.append(42.0)

arr3 = bytes((0, 1, 2, 3))