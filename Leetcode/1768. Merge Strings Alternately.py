class Solution:
    def mergeAlternately(self, word1, word2):
        merged_word = str()
        len1, len2, left1, left2 = len(word1), len(word2), 0, 0
        while left1 < len1 and left2 < len2:
            merged_word += word1[left1] + word2[left2]
            left1 += 1
            left2 += 1
        if left1 < len1:
            merged_word += word1[left1:]
        else:
            merged_word += word2[left2:]
        return merged_word
    
word1, word2 = input(), input()
obj = Solution()
print(obj.mergeAlternately(word1, word2))