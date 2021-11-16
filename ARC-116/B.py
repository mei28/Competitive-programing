n = int(input())
A = list(map(int, input().split()))
MOD = 998244353

A.sort()

result = 0

# ひとつしかないとき
for i in range(n):
    result = (result + A[i] ** 2) % MOD

# 二つ以上のとき

mult = 0
for min_i in range(n - 2, -1, -1):
    mult = (mult * 2 + A[min_i + 1]) % MOD

    result = (result + A[min_i] * mult) % MOD

print(result)
