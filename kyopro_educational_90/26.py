def dfs(pos: int, cur: int) -> None:
    # 二部グラフを見つける
    col[pos] = cur
    for i in G[pos]:
        if col[i] == -1:
            dfs(i, 1 - cur)


if __name__ == "__main__":
    N = int(input())
    G = [[] for _ in range(N + 1)]
    col = [-1] * (N)
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    # Graph Coloring
    dfs(0, 0)

    G1, G2 = [], []
    ans = []

    for i in range(N):
        if col[i] == 0:
            G1.append(i)
        else:
            G2.append(i)

    if len(G1) > len(G2):
        for i in range(N // 2):
            ans.append(G1[i + 1])
    else:
        for i in range(N / 2):
            ans.append(G2[i + 1])

    print(*ans)
