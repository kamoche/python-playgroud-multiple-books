def solution(N):
    # write your code in Python 3.6
    if 1 > N > 2147483647:
        return 0
    binary = format(N, 'b')
    print(binary)

    max_gap = 0
    ind = 0
    for x in range(len(binary)):
        if binary[x] == '1' and x != 0:
            max_gap = max((x - ind - 1), max_gap)
            ind = x
    return max_gap


# print(solution(1041))
print(solution(15))
