N = int(input())
AB = []

for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

AB = sorted(AB, key=lambda x: x[1])

i = 0
for a, b in AB:
    i += a
    if i > b:
        print("No")
        exit()

print("Yes")
