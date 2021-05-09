from collections import Counter

n = int(input())
s = input()
MOD = 1000000007

cnter = Counter(s)


ans = 1
for k, v in cnter.items():
    ans *= v + 1
    ans %= MOD

print((ans + MOD - 1) % MOD)
