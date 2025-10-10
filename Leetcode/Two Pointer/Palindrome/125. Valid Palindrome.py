class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = ''.join(a for a in s if a.isalnum())    # Alphanumaric_1st
        # s = ''.join(filter(str.isalnum,s)).lower()   # Alphanumaric_2nd
        # S = ''           # Alphanumaric_3rd
        # for a in s:
        #     if ('a' <= a <= 'z') or ('1' <= a <= '9'):
        #         S += a

        # Approach 1
        if s == s[::-1]: # ''.join(reversed(s))
            return True
        else:
            return False
        
        # Approach 2
        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     if s[l] != s[r]:
        #        return False
        #     l += 1
        #     r -= 1
        # return True

        # Approach 3
        # return s == ''.join(reversed(s))

s = input()
obj = Solution()
print(obj.isPalindrome(s))