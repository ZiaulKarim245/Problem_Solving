class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        cnt = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                cnt += 1
                left +=1 
                right -= 1
        return cnt

nums = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.maxOperations(nums, k))