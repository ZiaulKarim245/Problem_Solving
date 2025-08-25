class Solution:
    def mergeArrays(self, nums1, nums2):
        left1, left2 = 0, 0
        result = []
        n, m = len(nums1), len(nums2)
        while left1 < n and left2 < m:
            if nums1[left1][0] == nums2[left2][0]:
                result.append([nums1[left1][0],nums1[left1][1] + nums2[left2][1]])  
                left1 += 1
                left2 += 1
            elif nums1[left1][0] > nums2[left2][0]:
                result.append(nums2[left2])
                left2 += 1
            else:
                result.append(nums1[left1])
                left1 += 1
        while left1 < n:
            result.append(nums1[left1])
            left1 += 1
        while left2 < m:
            result.append(nums2[left2])
            left2 += 1
        return result
# nums1,  nums2 = [], []
n, m = 3, 3

# while n > 0:
#     nums1.append(list(map(int, input().split())))
#     n -= 1

# while m > 0:
#     nums2.append(list(map(int, input().split())))
#     m -= 1

nums1 = [list(map(int, input().split())) for _ in range(n)]
nums2 = [list(map(int, input().split())) for _ in range(m)]

obj = Solution()
print(obj.mergeArrays(nums1, nums2))