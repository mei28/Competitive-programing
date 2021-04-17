N, H = map(int, input().split())
a = []
b = []
for i in range(N):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

maxA = max(a)
b.sort()
b.reverse()

ans = 0
index = 0
for throwedKatana in b:
    if throwedKatana < maxA:
        break
    H -= throwedKatana
    ans += 1
    if H <= 0:
        break
if H > 0:
    ans += H // maxA
    if H % maxA != 0:
        ans += 1
print(ans)
