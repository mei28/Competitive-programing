n = int(input())
A = [input() for _ in range(n)]

B = []

for i, a in enumerate(A):
    if i == 0:
        tmp = A[1][0] + a[0 : n - 1]
        B.append(tmp)
    elif i == n - 1:
        tmp = a[1:n] + A[n - 2][-1]
        B.append(tmp)
    else:
        tmp = A[i + 1][0] + a[1 : n - 1] + A[i - 1][-1]
        B.append(tmp)

for b in B:
    print(b)
