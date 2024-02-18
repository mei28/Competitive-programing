N = int(input())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0

for a, b in zip(A, B):
    n = b - a + 1
    ans += (a + b) * n // 2
print(ans)
