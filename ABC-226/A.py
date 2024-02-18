x = input()
x = x.replace(".", "")

ans = int(x[:-3])

if int(x[-3]) >= 5:
    ans += 1

print(ans)
