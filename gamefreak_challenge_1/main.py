import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # step = int(lines[0])
    # if step == 1:
    #     step1(lines)

    step = int(lines[0])
    if step == 1:
        N = int(lines[1])
        A = list(map(int, lines[2].split(" ")))
        S_A = [0] * (N + 1)
        for i in range(N):
            S_A[i + 1] = S_A[i] + A[i]

        ans = 0
        for d in range(N):
            ret = S_A[d + 1] * (N - d - 1)
            ans = max(ret, ans)
        print(ans)
    elif step == 2:
        N = int(lines[1])
        A = list(map(int, lines[2].split(" ")))
        A.sort()
        A = A[::-1]
        S_A = [0] * (N + 1)
        for i in range(N):
            S_A[i + 1] = S_A[i] + A[i]

        ans = 0
        for d in range(N):
            ret = S_A[d + 1] * (N - d - 1)
            ans = max(ret, ans)
        print(ans)
    elif step == 3:
        N = int(lines[1])
        A = list(map(int, lines[2].split(" ")))
        S_A = [0] * (N + 1)
        for i in range(N):
            S_A[i + 1] = S_A[i] + A[i]

        ans = 0
        for d in range(N):
            ret = S_A[d + 1] * (N - d - 1)
            ans = max(ret, ans)
        print(ans)
    elif step == 4:
        N = int(lines[1])
        A = list(map(int, lines[2].split(" ")))
        S_A = [0] * (N + 1)
        for i in range(N):
            S_A[i + 1] = S_A[i] + A[i]

        ans = 0
        for d in range(N):
            ret = S_A[d + 1] * (N - d - 1)
            ans = max(ret, ans)
        print(ans)
    else:
        N = int(lines[1])
        A = list(map(int, lines[2].split(" ")))
        S_A = [0] * (N + 1)
        for i in range(N):
            S_A[i + 1] = S_A[i] + A[i]

        ans = 0
        for d in range(N):
            ret = S_A[d + 1] * (N - d - 1)
            ans = max(ret, ans)
        print(ans)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
