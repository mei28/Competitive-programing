S = input()
T = input()


def s_to_n(st):
    tmp = 0
    res = []

    s2n = dict()

    for c in st:
        if c not in s2n:
            s2n[c] = tmp
            tmp += 1
        res.append(s2n[c])
    return res


if s_to_n(S) == s_to_n(T):
    print("Yes")
else:
    print("No")
