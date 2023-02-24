n, k, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
for i in range(n):
    a = A[i]
    m = a // x

    if m > k:
        m = k
    k -= m
    A[i] = A[i] - x * m
    if k == 0:
        break


A.sort(reverse=True)
for i in range(n):
    a = A[i]
    m = -(-a // x)

    if m > k:
        m = k
    k -= m
    A[i] = max(0, A[i] - x * m)
    if k == 0:
        break
print(sum(A))
