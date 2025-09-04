class Solution:
    def beautifulIndices(self, s, a, b, k):
        result = []
        # len_s, len_a, len_b = len(s), len(a), len(b)
        # for i in range(len_s - len_a + 1):
        #     if s[i:i + len_a] == a:
        #         left, right = max(0, i - k), min(len_s - len_b, i + k)
        #         if b in s[left:right + len_b]:
        #             result.append(i)

        i, j = s.find(a), s.find(b)
        while i != -1:
            while j != -1:
                if max(0,i - k) <= j <= i + k:
                    result.append(i)
                    break
                if j > i + k:
                    break
                j = s.find(b,j + 1)
            i = s.find(a,i + 1)
        return result

s, a, b = input().split()
k = int(input())
obj = Solution()
print(obj.beautifulIndices(s, a, b, k))