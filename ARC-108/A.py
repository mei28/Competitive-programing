S, P = map(int, input().split())

for n in range(1, 9999999):
    if n * (S - n) == P:
        print("Yes")
        exit()

print("No")
