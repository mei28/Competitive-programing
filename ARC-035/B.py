MOD = 1000000007
n = int(input())
T = [int(input()) for _ in range(n)]
T.sort()

from collections import Counter

dct = Counter(T)


fact = [1]

for i in range(1, n + 1):
    fact.append((fact[-1] * i) % MOD)


ans1 = 0

for i, t in enumerate(T):
    ans1 += t * (n - i)

ans2 = 1
for v in dct.values():
    ans2 = (ans2 * fact[v]) % MOD

print(ans1)
print(ans2)
