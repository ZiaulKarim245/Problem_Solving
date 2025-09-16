class Solution:
    def checkInclusion(self, s1, s2):

        # Approach 1
        # n, m = len(s2), len(s1)
        # i = 0
        # while i < n:
        #     if i + m <= n and sorted(s1) == sorted(s2[i:i + m]):
        #         return True
        #     i += 1
        # return False

        # Approach 2
        # n, m = len(s2), len(s1)
        # for i in range(n - m + 1):
        #     if sorted(s1) == sorted(s2[i:i + m]):
        #         return True
        # return False
        # Approach 3
        n, m = len(s2), len(s1)
        tar = [0] * 26
        res = [0] * 26
        for ch in s1:
            tar[ord(ch) - ord('a')] += 1
        for ch in s2[:m]:
            res[ord(ch) - ord('a')] += 1
        if tar == res:
            return True
        for i in range(m,n):
            res[ord(s2[i]) - ord('a')] += 1
            res[ord(s2[i - m]) - ord('a')] -= 1
            if tar == res:
                return True
        return False



s1 = input()
s2 = input()
obj = Solution()
print(obj.checkInclusion(s1, s2))