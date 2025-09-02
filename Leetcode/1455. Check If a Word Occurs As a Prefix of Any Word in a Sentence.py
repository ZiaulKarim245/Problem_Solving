class Solution:
    def isPrefixOfWord(self, sentence, searchword):
        sentence_list = list(sentence.split(' '))
        for i, a in enumerate(sentence_list):
            if searchword in a:
                j, k = 0, 0
                while k < len(searchword):
                    if a[j] != searchword[k]:
                        break
                    j += 1
                    k += 1
                if k == len(searchword):
                    return i + 1
        return -1
    
sentence = input()
searchword = input()
obj = Solution()
print(obj.isPrefixOfWord(sentence, searchword))