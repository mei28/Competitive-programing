n, r = map(int, input().split())

MOD = 10**9 + 7

fact = [0] * (n + 1)
inv = [0] * (n + 1)
fact_inv = [0] * (n + 1)

fact[0] = 1
fact[1] = 1
fact_inv[0] = 1
fact_inv[1] = 1
inv[1] = 1

# MOD = (MOD // i) * i + (MOD % i)
# 0 = (MOD // i) * i + (MOD % i)
# 0 = (MOD // i)  + (MOD % i) * i^-1
#  (MOD % i) * i^-1 = -(MOD // i)
#   i^-1 = -(MOD // i) * (MOD % i)^-1
#   i^-1 = MOD -(MOD // i) * (MOD % i)^-1 %MOD
for i in range(2, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    fact_inv[i] = (fact_inv[i - 1] * inv[i]) % MOD

# nCr = n!/r!*(n-r)!

print(fact[n] * fact_inv[n - r] * fact_inv[r] % MOD)
