n, m = map(int, input().split())

H = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if a > b:
        H[a] += 1
    elif b > a:
        H[b] += 1

cnt = 0
for h in H:
    if h == 1:
        cnt += 1

print(cnt)
