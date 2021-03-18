s = input()

l = ""
ans = 0
r = ""

for i in range(len(s)):
    r += s[i]
    if l != r:
        ans += 1
        l = r
        r = ""

print(ans)
