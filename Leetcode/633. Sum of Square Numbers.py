import math
class Solution:
    def judgeSquareSum(self, c):
        left, right = 0, int(math.sqrt(c))  # int(c**0.5)
        while left <= right:
            if left**2 + right**2 == c:
                return True
            elif left**2 + right**2 < c:
                left += 1
            else:
                right -= 1
        return False

c = int(input())
obj = Solution()
print(obj.judgeSquareSum(c))