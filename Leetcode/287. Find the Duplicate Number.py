class Solution:
    def findDuplicate(self, nums):

        # Approach 1
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]

        # Approach 2
        # res = set()
        # for a in nums:
        #     if a in res:
        #         return a
        #     res.add(a)

        # Approach 3
        res = [0] * len(nums)
        for a in nums:
            if res[a] == 1:
                return a
            res[a]  = 1




nums = list(map(int, input().split()))
obj = Solution()
print(obj.findDuplicate(nums))