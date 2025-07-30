class Solution:
    def strStr(self, haystack: str , needle: str) -> int:
        return haystack.find(needle)

haystack , needle = map(str,input().split())
obj = Solution()
print(obj.strStr(haystack,needle))