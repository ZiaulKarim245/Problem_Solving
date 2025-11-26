from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        max_num = deque()
        res = []
        for i, a in enumerate(nums):
            if max_num and max_num[0] < i - k + 1:
                max_num.popleft()
            while max_num and nums[max_num[-1]] < a:
                max_num.pop()
            max_num.append(i)
            if i >= k - 1:
                res.append(nums[max_num[0]])
        return res

nums = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.maxSlidingWindow(nums, k))