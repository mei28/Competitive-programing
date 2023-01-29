n = int(input())
c, a = 0, 0

for _ in range(n):
    s = input()
    if s == "For":
        c += 1
    else:
        a += 1

if c > a:
    print("Yes")
else:
    print("No")
