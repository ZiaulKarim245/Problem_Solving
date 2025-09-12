class Solution:
    def backspaceCompare(self, s, t):
        n, m = len(s), len(t)
        left1, left2 = 0, 0
        s_new, t_new = [], []
        while left1 < n:
            if s[left1] == '#':
                if s_new:
                    del s_new[-1]
            else:
                s_new.append(s[left1])
            left1 += 1
            
        while left2 < m:
            if t[left2] == '#':
                if t_new:
                    del t_new[-1]
            else:
                t_new.append(t[left2])
            left2 += 1
        return True if s_new == t_new else False

s, t = input(), input()
obj = Solution()
print(obj.backspaceCompare(s, t))