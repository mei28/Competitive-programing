from bisect import bisect_left, bisect_right


def solve(N, A, S):
    S += "X"  # sentinel
    A += [0]  # sentinel
    M = [0] * (N + 2)
    E = [0] * (N + 2)
    X = [0] * (N + 2)
    C = [[0] * 3 for _ in range(N + 2)]

    for i in range(N):
        M[i + 1] = M[i] + (S[i] == "M")
        E[i + 1] = E[i] + (S[i] == "E")
        X[i + 1] = X[i] + (S[i] == "X")
        for j in range(3):
            C[i + 1][j] = C[i][j] + (A[i] == j)

    M_idx = [i for i in range(N + 1) if S[i] == "M"]
    X_idx = [i for i in range(N + 1) if S[i] == "X"]

    ans = 0
    for i in range(N + 1):
        if S[i] != "E":
            continue
        l = bisect_right(M_idx, i)
        r = bisect_left(X_idx, i)
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                ml = bisect_right(M_idx, C[i][a] - 1)
                mr = bisect_left(M_idx, C[i][a])
                xl = bisect_right(X_idx, C[N + 1][b])
                xr = bisect_left(X_idx, C[N + 1][b] + 1)
                ans += max(0, min(l - ml, xr - r)) * a
                ans += max(0, min(mr - l, r - xl)) * b
    return ans


N = int(input())
A = list(map(int, input().split()))
S = input().strip()
print(solve(N, A, S))
