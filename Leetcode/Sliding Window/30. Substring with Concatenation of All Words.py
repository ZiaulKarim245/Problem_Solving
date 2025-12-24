from collections import defaultdict
class Solution:
    def findSubstring(self, s, words):
        ans = []
        l, m, n = len(s), len(words), len(words[0])

        # wordcount = Counter(words)

        wordcount = {}
        for a in words:
            if a in wordcount:
                wordcount[a] += 1
            else:
                wordcount[a] = 1

        # for i in range(l - m * n + 1):
        #     substr = Counter()
        #     for j in range(i, i + m * n, n):
        #         a = s[j : j + n]
        #         substr[a] += 1
        #     if wordcount == substr:
        #         ans.append(i)

        for i in range(n):
            start = i
            cnt = 0
            temp_result = defaultdict(int)
            for j in range(i, l - n + 1, n):
                word = s[j:j + n]
                if word in wordcount:
                    temp_result[word] += 1
                    cnt += 1
                    while temp_result[word] > wordcount[word]:
                        temp_result[s[start:start + n]] -= 1
                        cnt -= 1
                        start = start + n
                    if cnt == m:
                        ans.append(start)
                        temp_result[s[start:start + n]] -= 1
                        cnt -= 1
                        start = start + n
                else:
                    temp_result.clear()
                    cnt = 0
                    start = j + n
        return ans

s = input()
words = list(input().split())
obj = Solution()
print(obj.findSubstring(s, words))