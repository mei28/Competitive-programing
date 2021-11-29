from collections import defaultdict, Counter

h, w, c, q = map(int, input().split())

# row_dct = {i:{j:0 for j in range(1,c+1)}for i in range(h)}
# col_dct = {i:{j:0 for j in range(1,c+1)}for i in range(w)}
row_dct = {i: dict() for i in range(h)}
col_dct = {i: dict() for i in range(w)}


def show(i):
    print(f"----{i}----")
    for k, v in row_dct.items():
        print(v)

    print("---")
    for k, v in col_dct.items():
        print(v)
    print("--------")


_c = c
for i in range(q):
    t, n, c = map(int, input().split())
    n -= 1
    if t == 1:
        # 行をぬる
        row_dct[n] = row_dct.setdefault(n, {})
        for k in range(1, c + 1):
            row_dct[n][k] = 0
        row_dct[n][c] = w
        # 塗り替えられた列の更新
        for k, vs in col_dct.items():
            col_dct[k] = col_dct.setdefault(k, {})
            for kk, v in vs.items():
                col_dct[k][kk] = col_dct[k].setdefault(kk, 0)
                if kk == c:
                    col_dct[k][kk] += 1
                    continue
                if col_dct[k][kk] == 0 or col_dct[k][kk] == 1:
                    continue

                col_dct[k][kk] -= 1
        pass
    else:
        # 列をぬる
        col_dct[n] = col_dct.setdefault(n, {})
        for k in range(1, c + 1):
            col_dct[n][k] = 0
        col_dct[n][c] = h
        # 塗り替えられた列の更新
        for k, vs in row_dct.items():
            row_dct[k] = row_dct.setdefault(k, {})
            for kk, v in vs.items():
                row_dct[k][kk] = row_dct[k].setdefault(kk, 0)
                if kk == c:
                    row_dct[k][kk] += 1
                    continue
                if row_dct[k][kk] == 0 or row_dct[k][kk] == 1:
                    continue
                row_dct[k][kk] -= 1

ans = {i: 0 for i in range(1, c + 1)}
show(0)
for _, vs in row_dct.items():
    for i in range(1, _c + 1):
        ans[i] += vs[i]
for i in range(1, _c + 1):
    print(ans[i], end=" ")
