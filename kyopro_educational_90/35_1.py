if __name__ == "__main__":
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    q = int(input())
    Qs = []
    for i in range(q):
        tmp = list(map(int, input().split()))
        tmp = list(map(lambda x: x - 1, tmp))
        Qs.append(tmp)
