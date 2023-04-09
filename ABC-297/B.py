S = input()
bx, by = -1, -1
rx, ry = -1, -1
k_idx = S.index("K")

for i, s in enumerate(S):
    if s == "B" and bx < 0:
        bx = i
    elif s == "B" and bx >= 0:
        by = i
    if s == "R" and rx < 0:
        rx = i
    elif s == "R" and rx >= 0:
        ry = i


if bx % 2 == by % 2:
    print("No")
    exit()

if k_idx < rx or ry < k_idx:
    print("No")
    exit()
print("Yes")
