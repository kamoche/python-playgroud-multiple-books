from collections import deque
from queue import LifoQueue

plates = []

plates.append(1)
plates.append(2)
plates.append(3)

plates.pop()

s = deque()

s.append('eat')
s.append('sleep')
s.append('code')

# >>> s
# deque(['eat', 'sleep', 'code'])
# >>> s.pop()
# 'code'

s1 = LifoQueue()
s1.put('eat')
s1.put('sleep')
s1.put('code')

# >>> s.get()
# 'code'
