def solve(p: int):
    ok = 0
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if A[mid] < p:
            ok = mid
            pass
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Q = int(input())
    B = [int(input()) for _ in range(Q)]

    for b in B:
        idx = solve(b)

        if idx >= N - 1:
            print(abs(b - A[idx]))
        else:
            print(min(abs(b - A[idx]), abs(b - A[idx + 1])))
