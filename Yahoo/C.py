N, X, Y = map(int, input().split())
A = list(input().split())
B = list(input().split())

flip = False
if X <= 2 * Y:
    flip = True
A = [1 if i == "R" else 0 for i in A]
B = [1 if i == "R" else 0 for i in B]
# C = [0 if i == j else 1 for i, j in zip(A, B)]
C = [i - j for i, j in zip(A, B)]

cost = 0
fliped = False
if flip:
    for i in range(1, N):
        if fliped:
            fliped = False
            continue
        a = C[i - 1]
        b = C[i]
        if a * b < 0:
            tmp = B[i - 1]
            B[i - 1] = B[i]
            B[i] = tmp
            cost += X
            fliped = True
    C = [i - j for i, j in zip(A, B)]
    cost += sum([abs(i) for i in C]) * Y
else:
    cost = sum([abs(i) for i in C]) * Y

print(cost)
