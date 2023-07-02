from decimal import Decimal

N = int(input())
res = []
for i in range(N):
    a, b = map(Decimal, input().split())
    res.append((-a / (a + b), i + 1))

res.sort()

for r in res:
    print(r[1])
