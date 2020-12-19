T = int(input())


def solve(n, s, k):
    N = [0] * n
    N[s] = 1
    flg = False
    cnt = 0
    while sum(N) < 2 * n:
        _next = (s+k) % n
        s = _next
        N[_next] += 1
        cnt += 1
        if N[_next] >= 2:
            flg = False
            break

        if N[0] == 1:
            flg = True
            break
    if flg:
        return cnt
    else:
        return -1
    pass


N, S, K = [], [], []

for t in range(T):
    n, s, k = map(int, input().split())
    N.append(n)
    S.append(s)
    K.append(k)

for i in range(T):
    n = N[i]
    s = S[i]
    k = K[i]
    print(solve(n, s, k))
