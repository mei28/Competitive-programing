s = input()
n = len(s)

ans = n**2 * 2

for i, c in enumerate(s):
    if c == "U":
        ans -= n - i - 1
    elif c == "D":
        ans -= i
    ans -= 2

print(ans)
