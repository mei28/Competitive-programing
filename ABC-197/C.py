n = int(input())
a = list(map(int, input().split()))

ans = 10e10

for bit in range(0, 1 << (n - 1)):
    val = 0
    tmp = 0
    for j in range(n):
        tmp |= a[j]
        if (bit >> j) % 2 == 1 or j == n - 1:
            val ^= tmp
            tmp = 0
    ans = min(ans, val)

print(ans)
