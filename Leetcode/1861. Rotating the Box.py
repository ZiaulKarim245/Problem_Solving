class Solution:
    def rotateTheBox(self, boxGrid):
        

boxGrid = []
while True:
    line = input()
    if line == "":
        break
    row = list(map(str,line.split()))
    boxGrid.append(row)
obj = Solution()
print(obj.rotateTheBox(boxGrid))