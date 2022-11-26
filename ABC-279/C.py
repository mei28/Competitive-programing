h, w = map(int, input().split())
A = [input() for _ in range(h)]
B = [input() for _ in range(h)]

AT = []
BT = []

for i in range(w):
    tmp_a = []
    tmp_b = []
    for j in range(h):
        a = A[j][i]
        b = B[j][i]
        tmp_a.append(a)
        tmp_b.append(b)
    tmp_a = tuple(tmp_a)
    tmp_b = tuple(tmp_b)
    AT.append(tmp_a)
    BT.append(tmp_b)

AT = list(AT)
AT.sort()
BT = list(BT)
BT.sort()
print("Yes") if all([a == b for a, b, in zip(AT, BT)]) else print("No")
