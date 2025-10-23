class Solution:
    def maxVowels(self, s:str, k:int) -> int:
        cnt, n, max_v= 0, len(s), 0
        vowel = 'aeiou'
        for i in range(k):
            if s[i] in vowel:
                cnt += 1
        max_v = cnt
        for i in range(1, n - k + 1):
            if s[i + k - 1] in vowel:
                cnt += 1
            if s[i - 1] in vowel:
                cnt -= 1
            max_v = max(max_v, cnt)
        return max_v

s, k = input(), int(input())
obj = Solution()
print(obj.maxVowels(s, k))
