n = int(input())
X = input()
S = set()
x, y = 0, 0
S.add((x, y))
for s in X:
    if s == "R":
        x = x + 1
        y = y
    if s == "L":
        x = x - 1
        y = y
    if s == "U":
        x = x
        y = y + 1
    if s == "D":
        x = x
        y = y - 1
    if (x, y) in S:
        print("Yes")
        exit()
    S.add((x, y))
print("No")
