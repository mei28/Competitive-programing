n = int(input())
S = [list(input()) for _ in range(n)]
T = [list(input()) for _ in range(n)]


def rot(S):
    return list(zip(*S[::-1]))


def find_left_top(S: list):
    for i in range(n):
        for j in range(n):
            if S[i][j] == "#":
                return i, j


def is_same(S, T):
    Si, Sj = find_left_top(S)
    Ti, Tj = find_left_top(T)

    offset_i = Ti - Si
    offset_j = Tj - Sj

    for i in range(n):
        for j in range(n):
            ii = i + offset_i
            jj = j + offset_j

            if 0 <= ii < n and 0 <= jj < n:
                if S[i][j] != T[ii][jj]:
                    return False
            else:
                if S[i][j] == "#":
                    return False

    return True


cnt_S = sum(1 for i in range(n) for j in range(n) if S[i][j] == "#")
cnt_T = sum(1 for i in range(n) for j in range(n) if T[i][j] == "#")

for _ in range(4):
    if is_same(S, T):
        print("Yes")
        exit()
    S = rot(S)

print("No")
