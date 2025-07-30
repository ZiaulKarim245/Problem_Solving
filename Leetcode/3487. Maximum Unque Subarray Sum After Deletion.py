class Solution:
    def maxSum(self,nums):
        nums.sort()
        sum = nums[len(nums) - 1]
        for i in range(len(nums) - 2,-1,-1):
            if nums[i] != nums[i+1] and nums[i] > 0:
                sum += nums[i]
        return sum
    
nums = list(map(int,input().split()))
obj = Solution()
print(obj.maxSum(nums))