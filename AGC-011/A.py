N, C, K = map(int, input().split())
# T = [int(input()) for _ in range(N)]
T = []
for i in range(N):
    T.append(int(input()))

T.sort()

ans = 0
start = 0
member = 0
time = 0
for i in range(N):
    member += 1

    if start != 0:
        time = T[i] - start
    if time > K:
        member = 1
        start = T[i]
        time = 0
        ans += 1
    elif member >= C:
        member = 0
        time = 0
        start = 0
        ans += 1
    elif member == 1:
        start = T[i]
        time = 0


if member != 0:
    ans += 1
print(ans)
