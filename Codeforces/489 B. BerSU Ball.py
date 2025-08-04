n = int(input())
boys = list(map(int, input().split()))
boys.sort()
m = int(input())
girls = list(map(int, input().split()))
girls.sort()
cnt_pair = 0
for boy in boys:
    for j,girl in enumerate(girls):
        if abs(girl - boy) <= 1:
            cnt_pair += 1
            girls[j] = -1
            break
print(cnt_pair)