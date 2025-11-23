class Solution:
    def maxScore(self, carPoints, k):
        score = sum(carPoints[:k])
        max_score = score
        for i in range(1, k + 1):
            score -= carPoints[k - i]
            score += carPoints[-i]
            max_score = max(max_score, score)
        return max_score

carPoints = list(map(int, input().split()))
k = int(input())
obj = Solution()
print(obj.maxScore(carPoints, k))