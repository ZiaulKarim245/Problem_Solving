class Solution:
    def reversePrefix(self, word, ch):
        word_list = list(word)
        if ch in word_list:
            # index = word_list.index(ch)
            # word_list[:index + 1] = reversed(word_list[:index + 1])
            # word_list[:index + 1] = word_list[index::-1]
            left, right = 0, word_list.index(ch)
            while left < right:
                word_list[left], word_list[right]  = word_list[right], word_list[left]
                left += 1
                right -= 1
        return ''.join(word_list)
word, ch = input(), input()
obj = Solution()
print(obj.reversePrefix(word, ch))