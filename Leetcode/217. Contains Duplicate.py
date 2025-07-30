from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        # Solution 1
        '''nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False'''
        # Solution 2
        return len(set(nums)) != len(nums)
        # Solution 3
        '''freq = Counter(nums)
        for x in freq.values():
            if x > 1:
                return True
        return False'''

nums = list(map(int,input().split()))
obj = Solution()
obj.containsDuplicate(nums)
