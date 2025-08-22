class Solution:
    def sortArrayByParityII(self, nums):
        even, odd = 0, 1

        # Using new list
        # new_nums = [-1] * len(nums)
        # for i in range(len(nums)):
        #     if nums[i] % 2:
        #         new_nums[odd] = nums[i]
        #         odd += 2
        #     else:
        #         new_nums[even] = nums[i]
        #         even += 2
        # return new_nums

        # Using in-place
        while(even < len(nums) and odd < len(nums)):
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        return nums

nums = list(map(int, input().split()))
obj = Solution()
print(obj.sortArrayByParityII(nums))