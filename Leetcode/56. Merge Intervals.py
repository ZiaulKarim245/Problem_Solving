class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        n = len(intervals)
        left, right = intervals[0]
        for i in range(1,n):
            if intervals[i][0] <= right:
                right = max(right, intervals[i][1])
            else:
                result.append([left,right])
                left, right = intervals[i]
        result.append([left,right])
        return result


n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]
obj = Solution()
print(obj.merge(intervals))