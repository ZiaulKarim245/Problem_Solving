class Solution:
    def pancakeSort(self, arr):
        result = []
        for a in range(len(arr),1,-1):
            idx = arr.index(a)
            if idx + 1 == a:
                continue
            result.append(idx + 1)
            # arr = arr[idx::-1] + arr[idx + 1:]
            left, right = 0, idx
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            left, right = idx + 1, len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[left], arr[right]
                left += 1
                right -= 1
            result.append(a)
            # arr = arr[a - 1::-1] + arr[a:]
            left, right = 0, a - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            left, right = a + 1, len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[left], arr[right]
                left += 1
                right -= 1
        return result
    
arr = list(map(int, input().split()))
obj = Solution()
print(obj.pancakeSort(arr))