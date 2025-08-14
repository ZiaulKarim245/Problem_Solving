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
# def solve():
#     import sys
#     input = sys.stdin.readline

#     t = int(input())
#     results = []

#     for _ in range(t):
#         n = int(input())
#         arr = list(map(int, input().split()))

#         total = 0
#         current_max = arr[0]

#         for i in range(1, n):
#             # If the sign of current element matches current_max, update current_max if needed
#             if (arr[i] > 0 and current_max > 0) or (arr[i] < 0 and current_max < 0):
#                 if arr[i] > current_max:
#                     current_max = arr[i]
#             else:
#                 # Different sign detected, add current_max to total and reset
#                 total += current_max
#                 current_max = arr[i]

#         # Add the last max element
#         total += current_max
#         results.append(str(total))

#     print("\n".join(results))


# if __name__ == '__main__':
#     solve()
