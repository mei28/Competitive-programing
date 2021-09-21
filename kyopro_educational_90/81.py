def show():
    print("-" * 20)
    for a in G:
        print(*a)
    print("-" * 20)


if __name__ == "__main__":
    n, k = map(int, input().split())
    A, B = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    r = max(A) + 1
    c = max(B) + 1

    G = [[0] * (c + 1) for i in range(r + 1)]

    for i in range(n):
        G[A[i] + 1][B[i] + 1] += 1

    for i in range(1, r):
        for j in range(1, c):
            G[i][j] += G[i][j - 1]
    for i in range(r + 1):
        for j in range(c + 1):
            G[i][j] += G[i - 1][j]

    ans = 0
    for i in range(0, r - k):
        for j in range(0, c - k):
            tmp = G[i][j] + G[i + k - 1][j + k - 1] + G[i][j + k - 1] + G[i + k - 1][j]
            ans = max(ans, tmp)

    print(ans)
