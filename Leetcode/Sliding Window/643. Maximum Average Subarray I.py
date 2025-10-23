class Solution:
    def findMaxAverage(self, nums: list[int], k:int) -> float:
        average, sum, n = 0, 0, len(nums)
        for i in range(k):
            sum += nums[i]  # sum = sum(nums[:k])
        average = sum / k
        for i in range(1, n - k + 1):
            sum -= nums[i - 1]
            sum += nums[i + k - 1]
            average = max(average, sum / k) 
        return average

nums = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.findMaxAverage(nums, k))