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
        n, m = len(s2), len(s1)
        for i in range(n - m + 1):
            if sorted(s1) == sorted(s2[i:i + m]):
                return True
        return False



s1 = input()
s2 = input()
obj = Solution()
print(obj.checkInclusion(s1, s2))