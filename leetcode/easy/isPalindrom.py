class Solution:
    def isPalindrome(self, x: int) -> bool:
        left_p = 0
        right_p = len(str(x)) - 1
        strn = str(x)
        is_palindrome = False
        while True:
            if right_p < left_p:
                return is_palindrome
            else:
                if strn[left_p] == strn[right_p]:
                    is_palindrome = True
                    left_p += 1
                    right_p -= 1
                else:
                    return False


sol = Solution()

print(sol.isPalindrome(121))