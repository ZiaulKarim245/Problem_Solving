class Solution:
    def isStrictlyPalindromic(self,n):
        return False # It's impossible that every base from 2 to n-2 will be a palindrome

n = int(input()) # take input
obj = Solution()
print(obj.isStrictlyPalindromic(n))