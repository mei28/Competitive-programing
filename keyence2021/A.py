N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_max = [1]*N
a_max[0] = A[0]
now_max = 1
for i in range(1, N):
    a_max[i] = max(A[i], a_max[i-1])

now_max = A[0]*B[0]
for i in range(N):
    now_max = max(now_max, a_max[i]*B[i])
    print(now_max)
