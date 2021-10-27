n = int(input())
a = [0] + list(map(int, input().split()))
n += 1

accum_sum = a[:]
for i in range(1, n):
    accum_sum[i] += accum_sum[i - 1]

accum_max = accum_sum[:]

for i in range(1, n):
    accum_max[i] = max(accum_max[i], accum_max[i - 1])


ans = 0
now = 0

for i in range(1, n):
    ans = max(ans, now + accum_max[i])
    now += accum_sum[i]

print(ans)
