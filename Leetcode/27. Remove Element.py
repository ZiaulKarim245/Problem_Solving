class Solution:
    def removeElement(self, nums, k):

        # Approach 1
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] != k:
        #         result.append(nums[i])
        # nums[:len(nums)] = result
        # return len(result)

        # Approach 2
        # left, right = 0, len(nums)
        # while left < right:
        #     if nums[left] == k:
        #         nums.remove(nums[left])
        #         left -= 1
        #         right -= 1
        #     left += 1
        # return len(nums)

        # Approach 3
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != k:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt
        

nums = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.removeElement(nums, k))