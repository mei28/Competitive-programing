N, M = map(int, input().split())
ans = [0, 0]

for d in range(1, 10):
    x = 0
    for n in range(1, N + 1):
        x = (10 * x + d) % M
        if x == 0:
            ans = max(ans, [n, d])
n, d = ans
if n == 0:
    print(-1)
else:
    print(f"{d}" * n)
