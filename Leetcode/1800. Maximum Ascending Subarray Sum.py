class Solution:
    def maxAscendingSum(slef, nums):
        sum = nums[0]
        max_sum = sum
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                sum += nums[i]
            else:
                sum = nums[i] 
            max_sum = max(max_sum, sum)
        return max_sum

nums = list(map(int, input().split()))
obj = Solution()
print(obj.maxAscendingSum(nums))