class Solution:
    def solve(self):
        t = int(input())
        result = []
        for _ in range(t):
            n, k = map(int, input().split())
            s = input()
            w_count = 0
            for i in range(k):  
                if s[i] == 'W':
                    w_count += 1
            # w_count = s[:k].count('W')
            recolour = w_count 
            for i in range(k, n):
                if s[i] == 'W':
                    w_count += 1
                if s[i - k] == 'W':
                    w_count -= 1
                recolour = min(w_count, recolour)
            result.append(recolour)
        for x in result:
            print(x)

if __name__ == "__main__":
    obj = Solution()
    obj.solve()
