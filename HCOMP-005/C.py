n = int(input())
A = list(map(int, input().split()))
B = A[0]

for i in range(1, n):
    a = A[i]
    B = B ^ a

ans = []
for a in A:
    ans.append(a ^ B)
print(*ans)
