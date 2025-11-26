class Solution:
    def maximumSubarraySum(self, nums, k):
        Sum = 0
        max_sum = 0
        n = len(nums)
        store = set()
        start = 0
        for i in range(n):
            while nums[i] in store:
                Sum -= nums[start]
                store.remove(nums[start])
                start += 1
            Sum += nums[i]
            store.add(nums[i])
            if len(store) == k:
                max_sum = max(max_sum, Sum)
                Sum -= nums[start]
                store.remove(nums[start])
                start += 1
        return max_sum
        

nums = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.maximumSubarraySum(nums, k))