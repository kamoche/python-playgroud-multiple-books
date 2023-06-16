class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        print(n)
        for i in range(int(n / 2)):
            x = s[:i + 1]
            print(x)
            repeat_x_to_len_of_s = (x * (int(n / len(x)) + 1))[:n]
            print(repeat_x_to_len_of_s)
            if repeat_x_to_len_of_s == s and s[-len(x):] == x:
                return True
        return False

    def repeatedSubstringPattern1(self, s: str) -> bool:
        return s in (2 * s)[1:-1]


sol = Solution()
# print(sol.repeatedSubstringPattern1("aabaaba"))
# print(sol.repeatedSubstringPattern1("abcdabcd"))
# print(sol.repeatedSubstringPattern1("babbabbabbabbab"))
print(sol.repeatedSubstringPattern1("abc"))
