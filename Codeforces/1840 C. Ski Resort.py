# Counter Based techniques
t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    wea_for = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for idx, a in enumerate(wea_for):
        if a <= q:
            cnt += 1
        else:
            if cnt >= k:
                ans += (cnt - k + 1) * (cnt - k + 2) // 2
            cnt = 0
    if cnt >= k:
            ans += (cnt - k + 1) * (cnt - k + 2) // 2
    print(ans)

# Two Pointer / Sliding Window
t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    wea_for = list(map(int, input().split()))
    ans = 0
    left = 0

    while left < n:
        if wea_for[left] > q:
            left += 1
            continue
        right = left
        while right < n and wea_for[right] <= q:
            right += 1
        length = right - left
        if length >= k:
            ans += (length - k + 1) * (length - k + 2) // 2
        left = right
    print(ans)
