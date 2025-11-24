class Solution:
    def findRepeatedDnaSequences(self, s):
        ans, store = set(), set()
        n = len(s)
        for i in range(n - 9):
            if s[i : i + 10] in store:
                ans.add(s[i : i + 10])
            else:
                store.add(s[i : i + 10])
        return list(ans)

s = input()
obj = Solution()
print(obj.findRepeatedDnaSequences(s))