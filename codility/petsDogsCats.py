def solution(P, T, A, B):
    # write your code in Python 3.6
    print("original P = ", P)
    print("original T = ", T)
    T_C = list(T)
    b = 0
    for x in range(len(A)):
        if P == T:
            return True
        b += (B[x] - A[x])
        if P[A[x]] != T[A[x]]:
            T[A[x]], T[B[x]] = T[B[x]], T[A[x]]
            print("P = ", P)
            print("T = ", T)
    if b == len(A):
        return P == T_C[:: -1]


    # for y in range(0, len(P)):
    #     print("round =======", y)
    #     if P == T:
    #         return True
    #     for x in range(len(A)):
    #         T[A[x]], T[B[x]] = T[B[x]], T[A[x]]
    #         print("P = ", P)
    #         print("T = ", T)

    return P == T


# print(solution([1, 1, 2], [2, 1, 1], [0, 2], [1, 1]))
# print(solution([2, 2, 1, 1, 1], [1, 1, 1, 2, 2], [0, 1, 2, 3], [1, 2, 0, 4]))
print(solution([2, 2, 2, 2, 1, 1, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2], [0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]))
