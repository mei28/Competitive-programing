n, w = map(int, input().split())


A, B = [], []
AB = []

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append([a, b])

AB = list(sorted(AB, key=lambda x: x[0], reverse=True))
ans = 0
idx = 0
while w >= 0:
    val, wei = AB[idx][0], AB[idx][1]
    _w = min(w, wei)
    ans += _w * val
    w -= _w
    idx += 1
    if idx >= n:
        break

print(ans)
