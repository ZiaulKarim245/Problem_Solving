class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        start = 0
        store = set()
        for i, a in enumerate(s):
            while a in store:
                store.remove(s[start])
                start += 1
            max_len = max(max_len, (i - start + 1))
            store.add(a)
        return max_len

s = input()
obj = Solution()
print(obj.lengthOfLongestSubstring(s))