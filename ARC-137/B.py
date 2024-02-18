n = int(input())
A = list(map(int, input().split()))

pre_sum = [0]
mn, mx, y, x = 10**18, 0, 0, 10**18

for i in range(n):
    if A[i]:
        pre_sum.append(pre_sum[-1] + 1)
    else:
        pre_sum.append(pre_sum[-1] - 1)

for i in range(n + 1):
    y = max(y, pre_sum[i] - mn)
    x = min(x, pre_sum[i] - mx)
    mn = min(mn, pre_sum[i])
    mx = max(mx, pre_sum[i])

print(y - x + 1)
