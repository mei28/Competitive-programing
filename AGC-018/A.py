n, k = map(int, input().split())
A = list(map(int, input().split()))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


ma = max(A)
g = ma
for a in A:
    g = gcd(a, g)

if k <= ma and k % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
