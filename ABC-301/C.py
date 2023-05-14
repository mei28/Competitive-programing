import string

S = input()
T = input()

dct_S = {i: 0 for i in string.ascii_lowercase}
dct_T = {i: 0 for i in string.ascii_lowercase}
dct_S["@"] = 0
dct_T["@"] = 0
for s in S:
    dct_S[s] += 1
for t in T:
    dct_T[t] += 1

for k in dct_S.keys():
    if k == "@":
        pass
    else:
        s, t = dct_S[k], dct_T[k]

        if k not in "atcoder" and s != t:
            print("No")
            exit()
        if k in "atcoder":
            if s < t:
                dct_S["@"] -= t - s
            if s > t:
                dct_T["@"] -= s - t

        if dct_S["@"] < 0 or dct_T["@"] < 0:
            print("No")
            exit()
print("Yes")
