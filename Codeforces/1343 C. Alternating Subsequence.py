t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    pos, neg = 0, -2000000000
    for i in range(n):
        if a[i] > 0:
            pos = max(pos, a[i])
            if a[i-1] < 0 and i != 0:
                sum += neg
                neg = -2000000000
        else:
            neg = max(neg, a[i])
            if a[i-1] > 0 :
                sum += pos
                pos = 0
    if pos > 0:
        sum += pos
    if neg > - 2000000000:
        sum += neg
    print(sum)