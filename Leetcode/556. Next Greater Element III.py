class Solution:
    def nextGreaterElement(self, n):
        num = list(map(int, str(n)))
        right1 = len(num) - 2
        while right1 >= 0 and num[right1] >= num[right1 + 1]:
            right1 -= 1
        if right1 < 0:
            return -1 
        right2 = len(num) - 1
        while num[right2] <= num[right1]:
            right2 -= 1
        num[right1], num[right2] = num[right2], num[right1]
        num[right1 + 1:] = reversed(num[right1 + 1:])
        ans = int(''.join(map(str, num)))
        return ans if ans < 2**31 else -1
        
n = int(input())
obj = Solution()
print(obj.nextGreaterElement(n))