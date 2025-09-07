from collections import Counter
class Solution:
    def numTriplets(self, nums1, nums2):
        def ans(nums1, nums2):
            cnt = 0
            result = Counter()
            for i in range(len(nums2)):
                for j in range(i + 1, len(nums2)):
                    product = nums2[i] * nums2[j]
                    result[product]  += 1
            for i in range(len(nums1)):
                product = nums1[i]**2
                cnt += result[product]
            return cnt
        return ans(nums1, nums2) + ans(nums2, nums1)

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
obj = Solution()
print(obj.numTriplets(nums1, nums2))