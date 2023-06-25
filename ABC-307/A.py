n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    print(sum(A[i * 7 : (i + 1) * 7]))
