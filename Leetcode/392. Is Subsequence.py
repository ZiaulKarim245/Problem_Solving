class Solution:
    def isSubsequence(self, s, t):
        left1, left2 = 0, 0
        n, m = len(s), len(t)
        while left1 != n and left2 != m:
            if s[left1] == t[left2]:
                left1 += 1
            left2 += 1
        if left1 == n:
            return True
        else:
            return False

s, t = input(), input()
obj = Solution()
print(obj.isSubsequence(s, t))