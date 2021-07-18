n = int(input())
A = list(map(int, input().split()))
A.sort()

# mCr
m = A[-1]
diff = m
ans = 0
for i in range(n - 1):
    r = A[i]
    tmp = abs(m - r * 2)
    if tmp < diff:
        diff = tmp
        ans = r

print(m, ans)
