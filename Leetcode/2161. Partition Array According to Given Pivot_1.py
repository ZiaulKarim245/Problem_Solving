from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0]*len(nums)
        first = 0
        last = len(nums) - 1
        for i,j in zip(range(len(nums)),range(len(nums) - 1,-1,-1)):
            if nums[i] < pivot:
                ans[first] = nums[i]
                first += 1
            if nums[j] > pivot:
                ans[last] = nums[j]
                last -= 1
        while first <= last:
            ans[last] = pivot
            last -= 1
        return ans
nums = list(map(int,input().split()))
pivot = int(input())
obj = Solution()
print(obj.pivotArray(nums,pivot))