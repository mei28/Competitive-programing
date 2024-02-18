n, k = map(int, input().split())
X = list(map(int, input().split()))

res = 10**10

for left in range(n - k + 1):
    right = left + k - 1

    lr = abs(X[right] - X[left])

    l_f = abs(X[left]) + lr
    r_f = abs(X[right]) + lr

    res = min(res, l_f, r_f)

print(res)
