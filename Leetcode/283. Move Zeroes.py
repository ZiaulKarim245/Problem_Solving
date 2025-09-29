class Solution:
    def moveZeroes(self, nums):

        # Approach 1
        # new_nums = [0] * len(nums)
        # cnt = 0
        # for i in range(len(nums)):
        #     if nums[i]  != 0:
        #         nums[cnt] = nums[i]
        #         cnt += 1
        # nums[cnt:] = [0] * (len(nums) - cnt)
        # return nums

        # Approach 2
        # new_nums = []
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         new_nums.append(nums[i])
        # nums[:] = new_nums + [0] * (len(nums) - len(new_nums))
        # return nums

        # Approach 3
        Nums = []
        cnt_zeros = 0
        for a in nums:
            if a != 0:
                Nums.append(a)
            else:
                cnt_zeros += 1
        nums.clear()  # del nums[:]
        for i in range(cnt_zeros):
            Nums.append(0)
        nums.extend(Nums)
        return nums
    
nums = list(map(int, input().split()))
obj = Solution()
print(obj.moveZeroes(nums))