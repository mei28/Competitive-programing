n = int(input())
A = list(map(int, input().split()))
A.sort()

less_sum = 0

all_sum = sum(A)
ans = 1 << 40
for i in range(n):
    tmp = A[i] * n - 2 * (less_sum + (n - i) * A[i]) + all_sum * 2
    ans = min(ans, tmp)
    less_sum += A[i]

print(ans / 2 / n)
