import string


h, w = map(int, input().split())
alp = "." + string.ascii_uppercase

A = [list(map(int, input().split())) for _ in range(h)]

B = []
for C in A:
    tmp = ""
    for c in C:
        tmp += alp[c]
    B.append(tmp)

for t in B:
    print(t)
