n = int(input())
A = list(map(int, input().split()))
sum_A = sum([a**2 for a in A])

b = 0
for i in range(n):
    for j in range(i + 1, n):
        if i == j:
            continue
        b += A[i] * A[j]
print(2 * sum_A - 2 * b)
