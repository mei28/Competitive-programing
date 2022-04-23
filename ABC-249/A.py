a, b, c, d, e, f, x = map(int, input().split())

takahashi = 0
aoki = 0

y = x
while y > 0:
    n = a
    if y - a < 0:
        n = y
        y = 0
    y -= n
    takahashi += n * b
    y -= c

y = x
while y > 0:
    n = d
    if y - d < 0:
        n = y
        y = 0
    y -= n
    aoki += n * e
    y -= f

if takahashi > aoki:
    print("Takahashi")
elif takahashi == aoki:
    print("Draw")
elif takahashi < aoki:
    print("Aoki")
