class Solution:
    def sortArrayByParity(self, nums):
        left, n = 0, len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i], nums[left] = nums[left], nums[i] 
                left += 1
        return nums

nums = list(map(int, input().split()))
obj = Solution()
print(obj.sortArrayByParity(nums))