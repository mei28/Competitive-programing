N, X = map(int, input().split())

A = list(map(int, input().split()))

D = []

for a in A:
    D.append(abs(X - a))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


ans = D[0]
for d in D:
    ans = gcd(ans, d)
print(ans)
