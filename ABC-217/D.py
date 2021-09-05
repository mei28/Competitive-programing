L, Q = map(int, input().split())
C, X = [], []


for _ in range(Q):
    c, x = map(int, input().split())
    C.append(c)
    X.append(x)


cut_list = [0, L]


def lower_index(q, cut_list):
    ng = 0
    ok = len(cut_list)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if cut_list[mid] <= q:
            ng = mid
        else:
            ok = mid
    return ok


for c, x in zip(C, X):
    if c == 1:
        idx = lower_index(x, cut_list)
        cut_list.insert(idx, x)

    else:
        idx = lower_index(x, cut_list)
        left = cut_list[max(0, idx - 1)]
        right = cut_list[min(len(cut_list) - 1, idx)]

        print(right - left)
