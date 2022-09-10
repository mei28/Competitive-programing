n = int(input())
P = list(map(int, input().split()))

cnt = [0] * n
for i in range(n):
    for j in range(-1, 2):
        cnt[P[i] - (i + j) % n] += 1

ans = -1
for i in cnt:
    ans = max(ans, i)
print(ans)
