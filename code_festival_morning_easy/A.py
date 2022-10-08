n = int(input())
A = list(map(int, input().split()))
print((-A[0] + A[n - 1]) / (n - 1))
