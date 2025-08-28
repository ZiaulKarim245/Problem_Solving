class Solution:
    def findKDistantIndices(self, nums, key, k):
        result = []
        n = len(nums)
        right = 0
        for i in range(n):
            # Approach: 1
            # for j in range(i + k + 1):
            #     if j < n:
            #         if abs(i - j) <= k and nums[j] == key:
            #             result.append(i)
            #             break

            # Approach: 2
            if nums[i] == key:
                left = max(right, i - k)
                right = min(n, i + k + 1)
                for j in range(left, right):
                    result.append(j)
        return result

nums = list(map(int, input().split()))
key, k = map(int, input().split())
obj = Solution()
print(obj.findKDistantIndices(nums, key, k))