class Solution:
    def canPlaceFlowers(self,flowerbed: list[int],n:int) -> bool:
        count = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count +=  1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n

flowerbed , n= list(map(int,input().split())) , int(input())
obj = Solution()
print(obj.canPlaceFlowers(flowerbed,n))