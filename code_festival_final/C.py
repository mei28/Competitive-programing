a = int(input())


def n_to_10(X: str, n: int) -> int:
    """Xをn進数から10進数に"""
    out: int = 0
    for i in range(1, len(X) + 1):
        out += int(X[-i]) * (n ** (i - 1))
    return out


for i in range(10, 1000001):
    ret = n_to_10(str(i), i)
    if ret == a:
        print(i)
        exit()

print(-1)
