from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        fre = defaultdict(int)
        for a in t:
            fre[a] += 1
            