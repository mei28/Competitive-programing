from itertools import permutations

if __name__ == "__main__":
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]
    M = int(input())
    G = [[] for i in range(N)]

    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        G[x].append(y)
        G[y].append(x)

    ps = permutations(range(N), N)
    ans = 1000 * 100

    flg = True
    for p in ps:
        cost = A[p[0]][0]
        flg = True
        for idx in range(1, N):
            a, b = p[idx - 1], p[idx]
            if b in G[a] or a in G[b]:
                flg = False
                cost = 0
                break
            else:
                cost += A[b][idx]
        if flg:
            ans = min(ans, cost)

    if ans >= 1000 * 100:
        print(-1)
    else:
        print(ans)
