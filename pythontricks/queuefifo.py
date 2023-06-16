from collections import deque

from multiprocessing import Queue

s = deque()

s.append('eat')
s.append('sleep')
s.append('code')

# >>> s.popleft()
# eat


s1 = Queue()
s1.put('eat')
s1.put('sleep')
s1.put('code')

# >>> s.get()
# 'eat
#
# >>> q.get_nowait()
# queue.Empty
# >>> q.get()
# # Blocks / waits forever...


from queue import Queue

p = Queue()
p.put('eat')
p.put('sleep')
p.put('code')

# >>> p
# <multiprocessing.queues.Queue object at 0x1081c12b0>
# >>> p.get()
# 'eat'
# >>> p.get()
# # Blocks / waits forever...