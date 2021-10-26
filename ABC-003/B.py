S = input()
T = input()

flg = True
for s, t in zip(S, T):
    if s == t:
        continue

    if s == "@" and t != "@":
        if t in "atcoder":
            continue
        flg = False
    if s != "@" and t == "@":
        if s in "atcoder":
            continue
        flg = False
    if s != t:
        flg = False

if flg:
    print("You can win")
else:
    print("You will lose")
