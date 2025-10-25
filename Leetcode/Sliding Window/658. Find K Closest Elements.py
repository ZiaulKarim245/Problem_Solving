class Solution:
    def findClosestElements(self, arr, k, x):

        # Approach 1
        # arr.sort(key=lambda num: (abs(x - num),num))
        # return sorted(arr[:k])

        # Approach 2
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid 
        return arr[left:left + k]
            
arr = list(map(int, input().split()))
k, x = int(input()), int(input())
obj = Solution()
print(obj.findClosestElements(arr, k, x))