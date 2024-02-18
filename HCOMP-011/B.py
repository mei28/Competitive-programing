n = int(input())
A = list(map(int, input().split()))

B = [0] * (10**5 + 10)
margin = 3

for i in range(n):
    a = A[i] + margin
    B[a - 1] += 1
    B[a + 2] -= 1

for i in range(1, len(B)):
    B[i] += B[i - 1]

print(max(B))
