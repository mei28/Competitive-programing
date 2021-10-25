n = int(input())

n %= 30

A = ["1", "2", "3", "4", "5", "6"]
for i in range(n):
    A[i % 5], A[i % 5 + 1] = A[i % 5 + 1], A[i % 5]

print("".join(A))
