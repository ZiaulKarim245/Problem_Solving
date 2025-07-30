class Solution:
    def distMoney(self, money,children):
        if money < children:
            return -1
        money -= children
        if children - (money // 7) == 1 and money - (money // 7) * 7 == 3:
            return (money // 7) - 1
        elif children - (money // 7) == 0 and money - (money // 7) * 7 > 0:
            return (money // 7) - 1
        elif children < (money // 7):
            return children - 1
        else:
            return (money // 7)

money = int(input()) 
children = int(input())
obj = Solution()
max_eights = obj.distMoney(money,children)
print(max_eights)