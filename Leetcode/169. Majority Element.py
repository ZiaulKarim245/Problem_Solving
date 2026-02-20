class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n, maj_element, cnt = len(nums), 0, 1
        nums.sort()
        for i in range(1, n):
            if nums[i] != nums[i - 1] and cnt > n//2:
                maj_element = nums[i - 1]
                cnt = 0
            cnt += 1
        if cnt > n//2:
            maj_element = nums[n - 1]
        return maj_element