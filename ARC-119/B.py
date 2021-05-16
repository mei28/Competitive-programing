if __name__ == "__main__":
    N = int(input())
    S = input()
    T = input()

    if S.count("1") != T.count("1"):
        print(-1)
        exit()
    if S == T:
        print(0)
        exit()

    cnt_S, cnt_T = 0, 0
    _S, _T = [], []

    for i in range(N):
        s, t = S[i], T[i]
        if s == "0":
            _S.append(i)
        if t == "0":
            _T.append(i)

    cnt = 0
    for i, j in zip(_S, _T):
        if i != j:
            cnt += 1

    print(cnt)
