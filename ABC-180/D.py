X, Y, A, B = map(int, input().split())

exp = 0
while X * A < X + B and X * A < Y:
    exp += 1
    X *= A
exp += (Y - X - 1) // B
print(exp)
