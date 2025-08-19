class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans
    
nums = list(map(int, input().split()))
obj = Solution()
print(obj.threeSum(nums))