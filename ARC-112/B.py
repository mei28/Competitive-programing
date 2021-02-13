b, c = map(int, input().split())

segment = []
# x x
segment.append((b, b-c//2))
# x o
segment.append((-b, -(b-(c-1)//2)))
# o x
segment.append((-b, -b-(c-1)//2))
# o o
if c >= 2:
    segment.append((-b, -b-(c-1)//2))


imos = []

for (l, r) in segment:
    if l > r:
        l, r = r, l
    imos.append((l, +1))
    imos.append((r+1, -1))

last = -(1e20)
cnt = 0

imos.sort()

ans = 0
for (pos, diff) in imos:
    if cnt > 0:
        ans += pos-last
    last = pos
    cnt += diff

print(ans)
