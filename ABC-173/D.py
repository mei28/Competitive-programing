n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = A[0]

for i in range(n - 2):
    ans += A[i // 2 + 1]

print(ans)
