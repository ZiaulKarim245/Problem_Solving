t = int(input())
while t:  # for _ in range(t):
    n , k = map(int,input().split())
    blackboard = list(map(int,input().split()))
    score = 0
    i , j = 0 , len(blackboard) - 1
    blackboard.sort()
    while i < j:
        if blackboard[i] + blackboard[j] >  k:
            j -= 1
        elif blackboard[i] + blackboard[j] <  k:
            i += 1
        else:
            score += 1
            i += 1
            j -= 1
    print(score)
    t -= 1