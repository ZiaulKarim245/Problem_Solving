class Solution:
    def rotate(self, nums, k):

        # 1st Approach
        # for _ in range(k):
        #     nums.insert(0,nums[-1])
        #     nums.pop(-1)
        n = len(nums)
        k %= n

        # 2nd Approach
        # nums[:] = nums[-k:] + nums[:-k]

        # 3rd Approach
        if k:
            nums.reverse()
            nums[:k] = nums[k-1::-1]
            # nums[:k]  = reversed(nums[:k])
            nums[k:] = nums[-1:k - 1:-1]
            # nums[k:]  = reversed(nums[k:])

nums = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.rotate(nums, k))