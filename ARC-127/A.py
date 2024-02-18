n: int = int(input())

result: int = 0

for i in range(1, 16):
    start = int("1" * i)

    if start > n:
        break
    else:
        result += 1

    bottom = top = start

    while True:
        bottom *= 10

        top = (top + 1) * 10 - 1

        if n < bottom:
            break

        result += min(n, top) - bottom + 1

print(result)
