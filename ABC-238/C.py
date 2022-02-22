MOD = 998244353
n = int(input())

m = 0  # 桁数
_n = n
while _n > 0:
    m += 1
    _n //= 10

ans = 0

for i in range(m - 1):
    ans += ((1 + 9 * 10 ** i) * (9 * 10 ** i)) // 2
    ans %= MOD

# m-1桁までの総数
tmp = n - 10 ** (m - 1) + 1
ans += (1 + tmp) * tmp // 2
ans %= MOD
print(ans)
