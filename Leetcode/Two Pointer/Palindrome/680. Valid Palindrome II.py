class Solution:

    ### Approach 1 ###

    #def validPalindrome(self, text):
        # def is_palindrome(l, r):
        #     while l < r:
        #         if text[l] != text[r]:
        #             return False
        #         l += 1 
        #         r -= 1
        #     return True
        
        # i, j = 0, len(text) - 1
        # while i < j:
        #     if text[i] != text[j]:
        #         return is_palindrome(i + 1,j)  or is_palindrome(i, j - 1)
        #     i += 1
        #     j -= 1
        # return True

    ### Approach 2 ###

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                #if s[l:r] == ''.join(reversed(s[l:r])):
                if s[l:r] == s[l:r][::-1]:
                    return True
                #elif s[l+1:r+1] == ''.join(reversed(s[l+1:r+1])):
                elif s[l+1:r+1] == s[l+1:r+1][::-1]:
                    return True
                else:
                    return False
        return True
                    
text = input("Enter a text: ")
obj = Solution()
print(obj.validPalindrome(text))