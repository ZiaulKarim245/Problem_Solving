class Solution:
    def isPalindrome(self, text):
        text = text.lower()
        text = ''.join(a for a in text if a.isalnum())
        # text = ''.join(filter(str.isalnum,text)).lower()
        print(text)
        if text == text[::-1]: # ''.join(reverse(text))
            return True
        else:
            return False
        """
        i = 0
        j = len(text) - 1
        while i < j:
            if text[i] != text[j]:
               return False
            i += 1
            j -= 1
        return True
        """

text = input("Enter a text: ")
obj = Solution()
print(obj.isPalindrome(text))