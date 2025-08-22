class Solution:
    def sortArrayByParityII(self, nums):
        even, odd = 0, 1
        new_nums = [-1] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 and odd < len(nums):
                new_nums[odd] = nums[i]
                odd += 2
            else:
                new_nums[even] = nums[i]
                even += 2
        return new_nums

nums = list(map(int, input().split()))
obj = Solution()
print(obj.sortArrayByParityII(nums))