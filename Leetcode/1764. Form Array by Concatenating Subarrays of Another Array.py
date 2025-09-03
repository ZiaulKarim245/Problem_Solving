class Solution: 
    def canChoose(self, groups, nums):
        n = len(nums)
        left, i = 0, 0
        m = len(groups[left])
        while i < n - m + 1:
            if nums[i:i + m] == groups[left]:
                left += 1
                i += m - 1
                if left == len(groups):
                    return True
                m = len(groups[left])
            i += 1
        if left < len(groups):
            return False
        else:
            return True

groups = []
for _ in range(2):
    groups.append(list(map(int,input().split())))
nums = list(map(int, input().split()))
obj = Solution()
print(obj.canChoose(groups, nums))