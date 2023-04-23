n = int(input())
S = input()

i0 = -1
i1 = -1
o1 = -1
for i, s in enumerate(S):
    if s == "|" and i0 < 0:
        i0 = i
    if s == "|":
        i1 = i
    if s == "*":
        o1 = i

if i0 < o1 < i1:
    print("in")
else:
    print("out")
