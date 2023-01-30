n, q = map(int, input().split())
MOD = 998244353
S = input()
accum = [0] * (n + 1)

base = 1


def inv(x):
    return pow(x, MOD - 2, MOD)


for i in range(n):
    accum[i + 1] = accum[i] + base * (ord(S[i]) - ord("a") + 8) % MOD
    base = base * 101 % MOD


def get(l, r):
    return (accum[r] - accum[l - 1]) * inv(pow(101, l - 1, MOD)) % MOD


for _ in range(q):
    a, b, c, d = map(int, input().split())
    if get(a, b) == get(c, d):
        print("Yes")
    else:
        print("No")
