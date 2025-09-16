class Solution:
    def nextPermutation(self, nums):

        # Approach 1
        # right, right1, n = len(nums) - 1, len(nums) - 2, len(nums)
        # while right1 > -1:
        #     if nums[right1]  < nums[right]:
        #         min_num = 110
        #         while right < n:
        #             if nums[right] <= nums[right1]:
        #                 break
        #             min_num = min(min_num,nums[right])
        #             min_num = max(min_num,nums[right1])
        #             right += 1
        #         nums[right1], nums[right - 1] = nums[right - 1], nums[right1]
        #         print(nums)
        #         nums[right1 + 1:] = sorted(nums[right1 + 1:])
        #         return nums
        #     right -= 1
        #     right1 -= 1
        # nums.sort()
        # return nums

        # Approach 2
        



nums = list(map(int, input().split()))
obj = Solution()
print(obj.nextPermutation(nums))