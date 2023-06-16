class Solution:
    def reverse(self, x: int) -> int:
        num = x
        is_negative = 1
        if -2 ** 31 > x > 2 ** 31 - 1:
            return 0
        if num < 0:
            is_negative = -1
            num = abs(num)
        result = str(num)[::-1]
        result = int(result) * is_negative
        return result if -2 ** 31 < result < 2 ** 31 - 1 else 0

    def reverse2(self, x: int) -> int:
        reverse = 0

        while x > 0:
            print('x = %s', x)
            reverse = reverse * 10 + (x % 10)
            print(reverse)
            x = x // 10
        return reverse


sol = Solution()


# print(sol.reverse(123))
# print(sol.reverse(-123))
# print(sol.reverse(120))
# print(sol.reverse(2147483647))

print(sol.reverse2(123))
# print(sol.reverse2(-123))
# print(sol.reverse2(120))
# print(sol.reverse2(2147483647))
