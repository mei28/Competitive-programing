n, m, b = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
print(n * m * b + n * sum(C) + m * sum(A))
