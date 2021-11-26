S = int(input())

ans = 0
MOD = 10 ** 9 + 7
fact = [0] * 4400
invfact = [0] * 4400
fact[0] = 1
for i in range(1, 4400):
    fact[i] = fact[i - 1] * i % MOD

invfact[4400 - 1] = pow(fact[4400 - 1], MOD - 2, MOD)

for i in range(4400 - 1, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def nCk(n, k):
    return fact[n] * invfact[k] * invfact[n - k] % MOD


for n in range(1, S):
    if 3 * n > S:
        break
    ans += nCk(S - 3 * n + n - 1, n - 1)
    ans %= MOD
print(ans)
