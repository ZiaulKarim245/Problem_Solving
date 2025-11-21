class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        sum, count = 0, 0
        for i in range(k):
            sum += arr[i]
        if sum / k >= threshold:
            count += 1
        n = len(arr)
        for i in range(1, n - k + 1):
            sum -= arr[i - 1]
            sum += arr[i + k -1]
            if sum / k >= threshold:
                count += 1
        return count
    
arr = list(map(int, input().split()))
k, threshold = int(input()), int(input())
obj = Solution()
print(obj.numOfSubarrays(arr, k, threshold))