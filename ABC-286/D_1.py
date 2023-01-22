n, x = map(int, input().split())

ans = set()
ans.add(0)
for _ in range(n):
    a, b = map(int, input().split())
    tmp = ans.copy()
    for s in tmp:
        for i in range(b + 1):
            ans.add(s + a * i)
# print(ans)
if x in ans:
    print("Yes")
else:
    print("No")
