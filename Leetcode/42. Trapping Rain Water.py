class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        water_trapped = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
        return water_trapped

height = list(map(int, input().split()))
obj = Solution()
print(obj.trap(height))