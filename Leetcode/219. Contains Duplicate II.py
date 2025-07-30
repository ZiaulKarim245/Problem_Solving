class Solution:
    def containsNearbyDuplicate(self,nums,k):
        # Solution 1
        '''con_dup = {}
        for i,num in enumerate(nums):
            if num in con_dup and i - con_dup[num] <= k:
                return True
            con_dup[num] = i
        return False'''
        # Solution 2
        '''if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+1+k]:
                return True
        return False'''
        # Solution 3
        con_dup = set()
        for i in range(len(nums)):
            if nums[i] in con_dup:
                return True
            con_dup.add(nums[i])
            if len(con_dup) > k:
                con_dup.remove(nums[i - k])
        return False



nums , k= list(map(int,input().split())) , int(input())
obj = Solution()
print(obj.containsNearbyDuplicate(nums,k))