n, q = map(int, input().split())

card = [0] * (n + 1)

for _ in range(q):
    c, x = map(int, input().split())

    if c == 1:
        card[x] += 1
    if c == 2:
        card[x] += 2
    if c == 3:
        if card[x] >= 2:
            print("Yes")
        else:
            print("No")
