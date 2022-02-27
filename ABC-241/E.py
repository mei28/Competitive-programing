n,k = map(int,input().split())

A = list(map(int,input().split()))

x = 0
for i in range(k):
    x += A[x%n]

print(x)
