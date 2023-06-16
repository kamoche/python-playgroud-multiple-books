class Solution:
    def removeDuplicates(self, nums) -> int:
        counter = 1
        ind = 0
        p = 0
        for x in range(1, len(nums)):
            if nums[ind] != nums[x]:
                p +=1
                nums[p]=nums[x]
                ind = x
                counter += 1
        nums = nums[:counter]

        return counter if len(nums) >= 1 else 0

    def removeDuplicates1(self, nums) -> int:
        temp_set = sorted(set(nums))

        for i, j in enumerate(temp_set):
            nums[i] = j

        print(nums)
        return len(temp_set)


sol = Solution()
# print(sol.removeDuplicates([1, 2]))
# print(sol.removeDuplicates([1, 1, 2]))
# print(sol.removeDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(sol.removeDuplicates([1]))
# print(sol.removeDuplicates([]))
print(sol.removeDuplicates1([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))