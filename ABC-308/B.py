n, m = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

dct = {}
ps = set(C) - set(D)

for d, p in zip(D, P[1:]):
    dct[d] = p
for p in ps:
    dct[p] = P[0]

ans = 0
for c in C:
    ans += dct[c]
print(ans)
