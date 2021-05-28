N = int(input())
A = [sum(list(map(int, input().split()))) for _ in range(N)]

MOD = 1000000007
ans = 1
for a in A:
    ans *= a
    ans %= MOD
print(ans)
