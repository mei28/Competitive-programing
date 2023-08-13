from collections import deque

n, m = map(int, input().split())
S = input()
C = list(map(int, input().split()))

T = [[] for _ in range(m + 1)]

for c, s in zip(C, S):
    T[c].append(s)

D = [[] for _ in range(m + 1)]

for i in range(1, m + 1):
    t = T[i]
    s = [t[-1]] + t[:-1]
    D[i] = deque(s)

ans = ""

for c in C:
    a = D[c].popleft()
    ans += a
    pass
print(ans)
