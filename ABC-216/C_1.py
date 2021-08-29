n = int(input())
now = n
ans = []
for i in range(130):
    if now == 0:
        break
    if now % 2 == 0:
        ans.append("B")
        now //= 2
    else:
        ans.append("A")
        now -= 1
    if i >= 121:
        break

ans = ans[::-1]

print("".join(ans))
