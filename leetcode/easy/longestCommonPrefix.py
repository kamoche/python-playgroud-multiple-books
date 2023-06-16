class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len(strs) == 0 or len(strs) > 200:
            return ""
        if len(strs) == 1:
            return strs[0]
        result = ''
        min_str = min(strs, key=len)
        if len(min_str) == 0 or len(min_str) > 200:
            return ""
        for i in range(len(min_str)):
            for n in range(len(strs)):
                if min_str[i] != strs[n][i]:
                    return result
                else:
                    if n == len(strs) - 1:
                        result += min_str[i]
        
        return result


sol = Solution()

print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
print(sol.longestCommonPrefix([]))

'jack'.find()