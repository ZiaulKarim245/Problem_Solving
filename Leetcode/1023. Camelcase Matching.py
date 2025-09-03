class Solution:
    def camelMatch(self, queries, pattern):
        result = []
        n = len(queries)
        for i in range(n):
            left_queries = 0
            left_pattern = 0
            m = len(queries[i])
            o = len(pattern)
            while left_queries < m:
                if left_pattern < o and queries[i][left_queries] == pattern[left_pattern]:
                    left_pattern += 1
                    left_queries += 1
                elif queries[i][left_queries].isupper():
                    left_queries += 1
                    break
                else:
                    left_queries += 1
            if left_queries < m or left_pattern < o:
                result.append(False)
            else:
                result.append(True)
        return result



queries = list(input().split())
pattern = input()
obj = Solution()
print(obj.camelMatch(queries, pattern))