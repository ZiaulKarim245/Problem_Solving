class Solution:
    def sortedSquares(self, nums):

        # Approach 1
        # for i in range(len(nums)):
        #     nums[i] **= 2
        # nums.sort()

        # Approach 2
        result = [num ** 2 for num in nums]
        result.sort()
        return result

nums = list(map(int, input().split()))
obj = Solution()
print(obj.sortedSquares(nums))