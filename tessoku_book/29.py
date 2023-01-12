import sys

sys.setrecursionlimit(10**7)
a, b = map(int, input().split())
MOD = 10**9 + 7

ans = 0


def modpow(a, b, mod):
    if b == 0:
        return 1 % mod
    if b % 2 == 0:
        return modpow(a * a % mod, b // 2, mod)
    if b % 2 == 1:
        return modpow(a, b - 1, mod) * a % mod


ans = modpow(a, b, MOD)
print(ans)
