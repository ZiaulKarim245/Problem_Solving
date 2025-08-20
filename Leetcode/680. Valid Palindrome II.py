class Solution:
    def validPalindrome(self, text):
        def is_palindrome(l, r):
            while l < r:
                if text[l] != text[r]:
                    return False
                l += 1 
                r -= 1
            return True

        i, j = 0, len(text) - 1
        while i < j:
            if text[i] != text[j]:
                return is_palindrome(i + 1,j)  or is_palindrome(i, j - 1)
                """
                    if text[i:j+1] != text[j:i-1:-1]   # ''.join(reversed(text[i:j+1]))
                        return False
                    else:
                        return True
                """
            i += 1
            j -= 1
        return True
                    
text = input("Enter a text: ")
obj = Solution()
print(obj.validPalindrome(text))