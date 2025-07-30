class Solution:
    def duplicateZeros(self,arr):
        i , n = 0, len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i+1,0)
                i += 1
            i += 1
        if len(arr) > n:
            del(arr[n:])

arr = list(map(int,input().split()))
obj = Solution()
obj.duplicateZeros(arr)