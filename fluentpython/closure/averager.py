def make_averager():
    series = []

    def average(new_value):
        '''series is a free variable'''
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return average


# avg = make_averager()
#
# print(avg(0))
# print(avg(1))
# print(avg(2))


def make_averager2():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value

        return total / count

    return average


avg1 = make_averager2()
#
print(avg1(0))
print(avg1(1))
print(avg1(2))
