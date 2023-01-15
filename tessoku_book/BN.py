n = int(input())
LR = [tuple(map(int, input().split())) for _ in range(n)]
LR = list(sorted(LR, key=lambda x: x[1]))

ans = 0
last_time = 0
for i in range(n):
    if LR[i][0] < last_time:
        continue
    ans += 1
    last_time = LR[i][1]
print(ans)
