# import pdb
import sys

F = sys.stdin


n, m, q = map(int, F.readline().split())


T = [[0] * n for _ in range(m)]

for _ in range(q):
    s = F.readline().split()
    if s[0] == "1":
        nn = int(s[1])
        ans = 0
        for i in range(m):
            if T[i][nn - 1]:
                ans += n - sum(T[i])
        print(ans)

    else:
        nn, mm = int(s[1]), int(s[2])
        T[mm - 1][nn - 1] = 1
