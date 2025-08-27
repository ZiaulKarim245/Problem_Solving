class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            # if nums[i] == 0:
            #     nums.append(0)
            #     nums.pop(i)
            #     n -= 1
            #     continue
            i += 1
            result = [x for x in nums if x != 0]
            result = result + [0] * (n - len(result))
        return result


nums = list(map(int, input().split()))
obj = Solution()
print(obj.applyOperations(nums))