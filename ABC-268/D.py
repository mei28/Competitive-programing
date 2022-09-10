n, m = map(int, input().split())
S = [input() for _ in range(n)]
T = [input() for _ in range(m)]

S.sort()
T.sort()

remain: int = 16

for i in range(n):
    remain -= len(S[i])

remain -= n - 1
