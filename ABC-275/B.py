a, b, c, d, e, f = map(int, input().split())
MOD = 998244353
ans1 = a * b
ans1 %= MOD
ans1 *= c
ans1 %= MOD

ans2 = d * e
ans2 %= MOD
ans2 *= f
ans2 %= MOD

ans = ans1 - ans2
ans %= MOD
print(ans)
