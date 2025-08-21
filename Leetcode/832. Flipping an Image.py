class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)
        for i in range(n):
            # image[i] = image[i][::-1]
            left, right = 0, n - 1
            while left < right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image


image = []
n = int(input())
for _ in range(n):
    ima = list(map(int, input().split()))
    image.append(ima)
obj = Solution()
print(obj.flipAndInvertImage(image))