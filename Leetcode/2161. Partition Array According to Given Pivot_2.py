from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # List comprehension
        first = [nums[i] for i in range(len(nums)) if nums[i] < pivot]
        last = [nums[i] for i in range(len(nums)) if nums[i] > pivot]
        equal = [nums[i] for i in range(len(nums)) if nums[i] == pivot]
        ## For Loop
        # first, equal, last = [],[],[]
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         first.append(nums[i])
        #     elif nums[i]  == pivot:
        #         equal.append(nums[i])
        #     elif nums[i] > pivot:
        #         last.append(nums[i])
        return first + equal + last
nums = list(map(int,input().split()))
pivot = int(input())
obj = Solution()
print(obj.pivotArray(nums,pivot))