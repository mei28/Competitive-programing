def main():
    # 入力・下処理
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    # 計算・出力
    ans = 0
    for i in range(N-1):
        if A[i] + A[i+1] > x:
            d = A[i] + A[i+1] - x
            ans += d
            A[i+1] = max(0, A[i+1] - d)
            A[i] = max(0, x - A[i+1])
    print(ans)

if __name__ == "__main__":
    main()

