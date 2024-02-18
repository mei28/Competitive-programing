def binary_search(q: int, left: int):
    ok = left
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if L[mid] < q:
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    ans = 0
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            k = binary_search(L[i] + L[j], j)
            ans += max(0, k - j)

    print(ans)
