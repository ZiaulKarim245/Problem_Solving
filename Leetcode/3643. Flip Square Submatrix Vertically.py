class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        for i in range(y, y + k):
            left, right = x, x + k - 1
            while left < right:
                grid[left][i], grid[right][i] = grid[right][i], grid[left][i]
                left += 1
                right -= 1
        return grid

grid = []
m = int(input())
for _ in range(m):
    grid.append(list(map(int, input().split())))
x, y, k = int(input()), int(input()), int(input())
obj = Solution()
print(obj.reverseSubmatrix(grid, x, y, k))