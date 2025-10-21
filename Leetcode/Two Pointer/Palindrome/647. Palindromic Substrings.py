class Solution:
    def countSubstrings(self, s):
        n = len(s)

        # Approach 1
        # cnt = n
        # i = 0
        # while i < n:
        #     j = i + 1
        #     while j < n:
        #         if i:
        #             if s[i:j + 1] == s[j:i - 1:-1]: # s[i:j + 1] == ''.join(reversed(s))
        #                 cnt += 1
        #         else:
        #             if s[i:j + 1] == s[j::-1]:
        #                 cnt += 1
        #         j += 1 
        #     i += 1
        # return cnt

        # Approach 2
        def palindrome(left, right):
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt
        result = 0
        for i in range(n):
            result += palindrome(i, i)
            result += palindrome(i, i + 1)
        return result

s = input()
obj = Solution()
print(obj.countSubstrings(s))