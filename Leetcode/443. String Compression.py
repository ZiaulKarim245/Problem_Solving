class Solution:
    def compress(self, chars):
        s = '' + chars[0]
        n, cnt = len(chars), 1
        for i in range(1,n):
            if chars[i] == chars[i - 1]:
                cnt += 1
            else:
                if cnt > 1:
                    s += str(cnt)
                s += chars[i]
                cnt = 1
        if cnt > 1:
            s += str(cnt)
        chars[:len(s)] = list(s)
        return len(s)


chars = list(input())
obj = Solution()
print(obj.compress(chars))