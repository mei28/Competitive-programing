n = int(input())
C = list(map(int, input().split()))
MOD = 1000000007

ans = 1
C.sort()

for i, c in enumerate(C):

    ans = ans * (c - i) % MOD

print(ans)
