class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        ans = ''

        # Approach 1
        # i = 0
        # while i < n:
        #     j = i + 1
        #     while j < n + 1:
        #         if s[i:j] == s[i:j][::-1]:
        #             if len(s[i:j]) > len(ans):
        #                 ans = s[i:j]
        #         j += 1
        #     i += 1
        # return ans

        # Approach 2
        def palindrome(l, r):
            while r < n and l >= 0 and s[l] == s[r]:
                r += 1
                l -= 1
            return s[l + 1:r]
        i = 0
        while i < n:
            temp = palindrome(i, i)
            if len(temp) > len(ans):
                ans = temp
            temp = palindrome(i, i + 1)
            if len(temp) > len(ans):
                ans = temp
            i += 1
        return ans

s = input()
obj = Solution()
print(obj.longestPalindrome(s))