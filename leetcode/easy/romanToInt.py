class Solution:
    def romanToInt(self, s: str) -> int:
        rom_cast = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        rom_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        x = 0
        while x < len(s):
            if x + 1 < len(s) and (s[x]+s[x + 1]) in rom_cast:
                result += rom_cast[s[x]+s[x + 1]]
                x += 2
            else:
                result += rom_symbol[s[x]]
                x += 1
        return result



sol = Solution()

# print(sol.romanToInt('III'))
print(sol.romanToInt('XLI'))
# print(sol.romanToInt('IX'))
# print(sol.romanToInt('LVIII'))
# print(sol.romanToInt('MCMXCIV'))
# print(sol.romanToInt("DCXXI"))
