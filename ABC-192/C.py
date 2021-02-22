n, k = map(int, input().split())


def next_number(x):
    str_x = "".join(sorted(list(str(x))))
    return int(str_x[::-1]) - int(str_x)


nn = n
loop = 0
i = 1
while i <= k:
    n = next_number(n)
    nn = next_number(next_number(nn))
    if n == nn and loop == 0:
        loop = i
    if loop != 0:
        if k % loop == i % loop:
            break
    i += 1

print(n)
