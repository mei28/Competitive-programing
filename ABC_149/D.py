def calc(x: str) -> None:
    if x == "r":
        return 0
    elif x == "s":
        return 1
    elif x == "p":
        return 2


def solve():
    ans = 0
    dp = [[0 for _ in range(3)] for _ in range(N + 10)]

    for i in range(N):
        for j in range(3):
            now = 0
            now_hand = calc(T[i])

            if i >= K:
                for l in range(3):
                    if j != l:
                        # k個前とは違うやつ
                        now = max(now, dp[i - K][l])
            # 勝とき
            if (j + 1) % 3 == now_hand:
                now += rsp[j]
            dp[i][j] = now

    for i in range(K):
        now = 0
        for j in range(3):
            now = max(now, dp[N - 1 - i][j])
        ans += now
    return ans


if __name__ == "__main__":
    N, K = map(int, input().split())
    rsp = list(map(int, input().split()))
    T = input()

    print(solve())
