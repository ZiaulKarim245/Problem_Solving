from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # # Approach 1: Sorting
        n, maj_element, cnt = len(nums), 0, 1
        # nums.sort()
        # # for i in range(1, n):
        # #     if nums[i] != nums[i - 1] and cnt > n//2:
        # #         maj_element = nums[i - 1]
        # #         cnt = 0
        # #     cnt += 1
        # # if cnt > n//2:
        # #     maj_element = nums[n - 1]
        # # return maj_element
        # return nums[n//2]
    
        # Approach 2: Hash Map
        count = defaultdict(int)
        n = n//2
        
        for num in nums:
            count[num] += 1
        for key, value in count.item():
            if value > n:
                return key
