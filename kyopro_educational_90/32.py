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

    ps_cost = []
    for p in ps:
        cost = 0
        for idx, a in enumerate(p):
            cost += A[a][idx]

        ps_cost.append([p, cost])

    ps_cost = sorted(ps_cost, key=lambda x: x[1])

    for p, cost in ps_cost:
        flg = True
        for i in range(1, N):
            a, b = p[i - 1], p[i]
            if b in G[a] or a in G[b]:
                flg = False
                break
        if flg:
            print(cost)
            exit()
    print(-1)
