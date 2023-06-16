class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p = s.count('(')
        right_p = s.count(')')
        asterisk = s.count('*')
        print(left_p)
        print(right_p)
        print(asterisk)
        dif = (left_p - right_p) if left_p > right_p else (right_p - left_p)
        print(dif)

        if dif == 0:
            return True
        else:
            return True if dif <= asterisk and left_p < right_p else False

sol = Solution()

# print(sol.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(sol.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))