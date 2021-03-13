def rle_comp(S: str) -> list:
    rle = []
    pre = "X"
    chain = 1
    for c in S:
        if c == pre:
            chain += 1
        else:
            if pre != "X":
                rle.append([pre, chain])

            pre = c
            chain = 1
    rle.append([pre, chain])

    # print(rle)
    return rle


N, A, B, C, D = map(int, input().split())
S = input()
ans = "Yes"
if C < D:
    rle = rle_comp(S[A - 1 : D])
    for i in range(len(rle)):
        if rle[i][0] == "#" and rle[i][1] >= 2:
            ans = "No"
else:
    rle = rle_comp(S[A - 1 : C])
    for i in range(len(rle)):
        if rle[i][0] == "#" and rle[i][1] >= 2:
            ans = "No"

    space = False
    rle = rle_comp(S[B - 2 : D + 1])
    for i in range(len(rle)):
        if rle[i][0] == "." and rle[i][1] >= 3:
            space = True

    if not space:
        ans = "No"

print(ans)
