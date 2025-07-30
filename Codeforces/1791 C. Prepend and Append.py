t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    start = 0
    end = n - 1
    while start < end and s[start] != s[end]:
        n -= 2
        start += 1
        end -= 1
    print(n)
