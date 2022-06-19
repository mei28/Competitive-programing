n = int(input())
LR = [list(map(int, input().split())) for _ in range(n)]

LR = list(sorted(LR, key=lambda x: x[0]))

ans = []

for l, r in LR:
    if ans == []:
        ans.append([l, r])
    else:
        if l <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], r)
        else:
            ans.append([l, r])

for l, r in ans:
    print(l, r)
