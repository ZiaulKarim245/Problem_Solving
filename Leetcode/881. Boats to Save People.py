class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        boats = 0
        n = len(people)
        left, right = 0, n - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1
        return boats 

people = list(map(int, input().split()))
limit = int(input())
obj = Solution()
print(obj.numRescueBoats(people, limit))