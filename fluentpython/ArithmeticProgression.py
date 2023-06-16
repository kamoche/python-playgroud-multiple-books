import itertools


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0

        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def generator_function(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


class MyCalendar:

    def __init__(self):
        self.current_booking = []

    def book(self, start: int, end: int) -> bool:

        if self.current_booking is None and end > start:
            self.current_booking.append(start)
            self.current_booking.append(end)
            return True
        if start in range(self.curent_booking[0], self.current_booking[1]):
            return True
        return False


cool_gen = itertools.takewhile(lambda x: x < 15, itertools.count(0, 1))

sp = ArithmeticProgression(0, 1, 20)

print(list(sp))
print(list(generator_function(0, 1, 20)))
print(list(cool_gen))
