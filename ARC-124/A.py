N, K = map(int, input().split())
a = [0] * N
b = [0] * N

for i in range(K):
    c, k = input().split()
    k = int(k) - 1
    b[k] = 1

    for j in range(N):
        if c == "L" and k <= j:
            a[j] += 1
        if c == "R" and j <= k:
            a[j] += 1

MOD = 998244353

ans = 1
for i in range(N):
    if b[i] == 0:
        ans = ans * a[i] % MOD

print(ans)
