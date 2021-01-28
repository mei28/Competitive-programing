import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    lines = list(map(int, lines[0].split()))

    N = lines[0]
    M = lines[1]

    A = [0] * N
    C = [0] * N

    for i in range(N):
        A[i] = lines[2*i+2]
        C[i] = lines[2*i+3]

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    # dp
    for i, (a, c) in enumerate(zip(A, C)):
        for j in range(M+1):
            dp[i+1][j] = dp[i][j]
            if j-c >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-c]+a)

    print(dp[-1][-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
