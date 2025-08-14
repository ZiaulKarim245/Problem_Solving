class Solution:
    def removeDuplicates(self, nums):
        dup = nums[0]
        count = 1
        for num in nums[1:]:
            if num == dup:
                count += 1
                if count > 2:
                    nums.remove(num)
            else:
                dup = num 
                count = 1
        return len(nums)

nums = list(map(int, input().split()))
obj = Solution()
print(obj.removeDuplicates(nums))