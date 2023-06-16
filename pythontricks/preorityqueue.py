from queue import PriorityQueue
q = []
q.append((2, 'code'))
q.append((1, 'eat'))
q.append((3, 'sleep'))
# NOTE: Remember to re-sort every time
# a new element is inserted, or use
# bisect.insort().
q.sort(reverse=True)
while q:
    next_item = q.pop()
print(next_item)

import heapq

p = []
heapq.heappush(p, (2, 'code'))
heapq.heappush(p, (1, 'eat'))
heapq.heappush(p, (3, 'sleep'))
while p:
    next_item = heapq.heappop(p)
print(next_item)
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')


w = PriorityQueue()
w.put((2, 'code'))
w.put((1, 'eat'))
w.put((3, 'sleep'))
while not w.empty():
    next_item = w.get()
print(next_item)
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
