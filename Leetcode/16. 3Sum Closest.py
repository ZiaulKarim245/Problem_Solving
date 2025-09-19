class Solution:
    def threeSumClosest(self, nums, target):

        # Approach 1
        # nums.sort()
        # closest_diff, closest_sum = 111111, 0
        # n = len(nums) - 2
        # for i in range(n):
        #     left, right = i + 1, len(nums) - 1
        #     while left < right:
        #         sum = nums[i] + nums[left] + nums[right]
        #         closest_sum = sum if abs(sum - target) < closest_diff else closest_sum
        #         closes_diff = min(closest_diff, abs(sum - target))
        #         if sum < target:
        #             left += 1
        #         else:
        #             right -= 1
        # return closest_sum

        # Approach 2
        nums.sort()
        closest = sum(nums[:3])
        n = len(nums) - 2
        for i in range(n):
            left, right = i + 1, len(nums) - 1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                closest = Sum if abs(Sum - target) < abs(closest - target) else closest
                if Sum - target == 0:
                    return target
                elif Sum < target:
                    left += 1
                else:
                    right -= 1
        return closest


nums = list(map(int, input().split()))
target = int(input())
obj = Solution()
print(obj.threeSumClosest(nums, target))