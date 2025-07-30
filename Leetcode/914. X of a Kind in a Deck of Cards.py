from collections import Counter
from math import gcd
from functools import reduce
class solution:
    def hasGroupsSizeX(self, deck):
        fre_count = {}
        for x in deck:
            if x in fre_count:
                fre_count[x] += 1
            else:
                fre_count[x] = 1
        # fre_count = Counter(deck)
        values = list(fre_count.values())
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        overall_gcd = values[0]
        for x in values[1:]:
            overall_gcd = gcd(overall_gcd,x)
        # overall_gcd = reduce(gcd,values)
        if overall_gcd > 1:
            return True
        else:
            return False

deck = list(map(int, input().split()))
obj = solution()
obj.hasGroupsSizeX(deck)
