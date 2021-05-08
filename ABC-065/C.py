from math import factorial

n, m = map(int, input().split())
MOD = 1000000007


if n == m:
    print((factorial(n) * factorial(m) * 2) % MOD)
elif abs(n - m) == 1:
    print((factorial(n) * factorial(m)) % MOD)
else:
    print(0)
