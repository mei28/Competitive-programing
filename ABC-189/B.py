N, X = map(int, input().split())
V, P = [], []


ans = 0
for i in range(N):
    v, p = map(int, input().split())
    tmp = v * p
    ans += tmp
    if ans > X * 100:
        print(i + 1)
        exit()

print(-1)
