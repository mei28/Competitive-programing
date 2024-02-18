x = list(input())
i = 0
v = -1
x.sort()
for i, v in enumerate(x):
    if v != "0":
        break
x.remove(v)
x = [v] + x
print(int("".join(x)))
