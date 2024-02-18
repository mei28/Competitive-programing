if __name__ == "__main__":
    N, M = map(int, input().split())
    A, B, C = [], [], []
    G = dict()
    for i in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)

        G[a] = G.setdefault(a, []) + [b, c]
        G[b] = G.setdefault(b, []) + [a, c]

    print(G)
