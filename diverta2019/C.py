n = int(input())
cnt = 0
S = []
for i in range(n):
    s = input()
    cnt += s.count("AB")
    S.append(s)

x, y, z = 0, 0, 0
for s in S:
    if s[0] == "B" and s[-1] == "A":
        x += 1
    elif s[-1] == "A":
        y += 1
    elif s[0] == "B":
        z += 1

if x > 0:
    if y == 0 and z == 0:
        cnt += x - 1
    elif y == 0 or z == 0:
        cnt += x
    else:
        cnt += x + 1 + min(y - 1, z - 1)
else:
    cnt += min(y, z)

print(cnt)
