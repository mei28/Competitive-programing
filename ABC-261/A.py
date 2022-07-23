a, b, c, d = map(int, input().split())
l = max(a, c)
r = min(b, d)

if r >= l:
    print(abs(r - l))
else:
    print(0)
