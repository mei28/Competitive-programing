n, x, y, z = map(int, input().split())


a = min(x, y)
b = max(x, y)

for i in range(a, b + 1):
    if i == z:
        print("Yes")
        exit()
print("No")
