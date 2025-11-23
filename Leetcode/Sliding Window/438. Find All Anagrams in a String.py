class Solution:
    def findAnagrams(self, s, p):

        # ************** Approach 1 ****************

        # S, P = list(s), list(p)
        # P = sorted(P)
        # l, L = len(P), len(S)
        # ans = []
        # for i in range(L - l + 1):
        #     if P == sorted(S[i: i + l]):
        #         ans.append(i)
        # return ans

        # ***************** Approach 2 ********************

        S = [0] * 26
        P = [0] * 26
        for a in p:
            P[ord(a) - 97] += 1
        n = len(p)
        start, end = 0, 0
        ans = []
        for a in s:
            S[ord(a) - 97] += 1
            end += 1
            if end - start == n:
                if S == P:
                    ans.append(start)
                S[ord(s[start]) - 97] -= 1
                start += 1
        return ans



s, p = input(), input()
obj = Solution()
print(obj.findAnagrams(s, p))