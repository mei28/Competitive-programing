N = int(input())
A = list(map(int, input().split()))
S = [0 for _ in range(N)]
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]
print(A)
print(S)
