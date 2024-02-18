n = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(n):
    if A[0] + i != A[i]:
        print(A[0] + i)
        exit()
