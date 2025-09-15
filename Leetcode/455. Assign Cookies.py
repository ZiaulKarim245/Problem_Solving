class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        left1, left2, cnt = 0, 0, 0
        n, m = len(g), len(s)
        while left1 < n and left2 < m:
            if s[left2] >= g[left1]:
                cnt += 1
                left1 += 1
                left2 += 1
            else: 
                left2 += 1
        return cnt

g = list(map(int, input().split()))
s = list(map(int, input().split()))
obj = Solution()
print(obj.findContentChildren(g, s))