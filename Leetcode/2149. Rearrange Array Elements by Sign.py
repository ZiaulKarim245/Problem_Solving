class Solution:
    def rearrangeArray(self, nums):
        new_nums = [0] * len(nums)
        pos_ind, neg_ind = 0, 1
        for num in nums:
            if num > 0:
                new_nums[pos_ind] = num
                pos_ind += 2
            else:
                new_nums[neg_ind] = num
                neg_ind += 2
        return new_nums

nums = list(map(int, input().split()))
obj = Solution()
print(obj.rearrangeArray(nums))