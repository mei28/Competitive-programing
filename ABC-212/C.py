n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

i, j = 0, 0

min_ans = 1 << 60
while i < n and j < m:
    a, b = A[i], B[j]
    min_ans = min(min_ans, abs(a - b))
    if a > b:
        j += 1
    else:
        i += 1

print(min_ans)
