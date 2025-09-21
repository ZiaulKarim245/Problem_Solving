class Solution:
    def removeDuplicates(self, nums):

        # Approach 1
        # result = []
        # for a in nums:
        #     if a not in result:
        #         result.append(a)
        # nums[:len(result)] = result
        # return len(result)

        # Approach 2
        # left, right, cnt = 0, 1, 1
        # n = len(nums)
        # while right < n:
        #     if nums[left] != nums[right]:
        #         cnt += 1
        #         left += 1
        #         nums[left] = nums[right]
        #     right += 1
        # return cnt

        # Approach 3
        cnt = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt 

nums = list(map(int, input().split()))
obj = Solution()
print(obj.removeDuplicates(nums))