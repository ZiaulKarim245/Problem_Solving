class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        l, h = 0, len(s)
        res = []
        for a in s:
            if a == 'I':
                res.append(l)
                l += 1
            else:
                res.append(h)
                h -= 1
        res.append(l)
        return res

s = input()
obj = Solution()
print(obj.diStringMatch(s))