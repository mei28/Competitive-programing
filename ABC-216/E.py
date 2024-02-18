def main():
    def judge(m):
        cnt = 0
        for x in A:
            if x >= m:
                cnt += x - m + 1
        return cnt <= K

    def solve(m):
        rem = K
        ans = 0
        for i in range(N):
            x = A[i]
            if x >= m:
                diff = x - m + 1
                ans += diff * (x + m) // 2  # 等差数列の和の公式
                rem -= diff
        ans += rem * (m - 1)
        return ans

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ok = 2 * 10**9 + 5
    ng = 0

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if judge(mid):
            ok = mid
        else:
            ng = mid
    print(solve(ok))


if __name__ == "__main__":
    main()
