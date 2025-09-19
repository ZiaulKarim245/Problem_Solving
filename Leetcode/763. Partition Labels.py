class Solution:
    def partitionLabels(self, s):
        last_idx = {c : i for i, c in enumerate(s)}
        left, right = 0, 0
        result = []
        for i, c in enumerate(s):
            right = max(right, last_idx[c])
            if i == right:
                result.append(right - left + 1)
                left = 1  + i
        return result
    
s = input()
obj = Solution()
print(obj.partitionLabels(s))