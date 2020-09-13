a, b, c, d = map(int, input().split())

if a < 0 and b < 0 and c < 0 and d < 0:
    print(a * c)
if a < 0 and b < 0 and c < 0 and d > 0:
    print(a * c)
if a < 0 and b < 0 and c > 0 and d > 0:
    print(b * c)

if a < 0 and b > 0 and c < 0 and d < 0:
    print(a * c)
if a < 0 and b > 0 and c < 0 and d > 0:
    print(max(a*c, b*d))
if a < 0 and b > 0 and c > 0 and d > 0:
    print(b * d)

if a > 0 and b > 0 and c < 0 and d < 0:
    print(a * d)
if a > 0 and b > 0 and c < 0 and d > 0:
    print(b * d)
if a > 0 and b > 0 and c > 0 and d > 0:
    print(b * d)

if a == 0:
    if c <= 0 and d <= 0:
        print(0)
    if c <= 0 and d > 0:
        print(b*d)
    if c > 0 and d > 0:
        print(b*d)
elif b == 0:
    if c <= 0 and d <= 0:
        print(a * c)
    if c <= 0 and d > 0:
        print(a * c)
    if c > 0 and d > 0:
        print(0)
elif c == 0:
    if a <= 0 and b <= 0:
        print(0)
    if a <= 0 and b > 0:
        print(d * b)
    if a > 0 and b > 0:
        print(d * b)
elif d == 0:
    if a <= 0 and b <= 0:
        print(a * c)
    if a <= 0 and b > 0:
        print(a * c)
    if a > 0 and b > 0:
        print(0)
