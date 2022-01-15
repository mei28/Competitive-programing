def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    A.sort()

    # 偶数個の場合
    if N % 2 == 0:
        plus = A[N//2:]
        minus = A[:N//2]

        result = 2 * sum(plus) - 2 * sum(minus)

        # 足す数は一番小さいものを、
        # 引く数は一番大きいものを端に持っていく
        result = result - plus[0] + minus[-1]

    # 奇数個の場合
    else:
        plus = A[N//2+1:]
        minus = A[:N//2]
        mid = A[N//2]

        tmp_r = 2 * sum(plus) - 2 * sum(minus)

        # 中央の数を足す方にする場合（大小大小～の並びになる）
        # 両端が足す数になる。足す数のうち小さいものから順に 2個
        # 端に移動するが、そのうち1つは中央の数
        res1 = (tmp_r + mid * 2) - mid - plus[0]

        # 中央の数を引く方にする場合（小大小大～の並びになる）
        # 両端が引く数に（以下略
        res2 = (tmp_r - mid * 2) + mid + minus[-1]

        # 比べて大きい方を取る
        result = max(res1, res2)

    print(result)

main()
