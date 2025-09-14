class Solution:
    def checkIfExist(self, arr):

        # Approach 1
        # n = len(arr)
        # arr.sort()
        # for i in range(n - 1):
        #     if arr[i] * 2 in arr[i + 1:] or arr[i] * 2 in arr[:i]:
        #         return True
        # return False

        # Approach 2
        if arr.count(0) > 1:
            return True
        for a in arr:
            if a != 0 and a * 2 in arr:
                return True
        return False

arr = list(map(int, input().split()))
obj = Solution()
print(obj.checkIfExist(arr))