k = int(input())
a, b = map(int, input().split())


def base_n_to_10(x: str, n: int) -> int:
    out: int = 0
    for i in range(1, len(x) + 1):
        out += int(x[-i]) * (n ** (i - 1))
    return out


_a = base_n_to_10(str(a), k)
_b = base_n_to_10(str(b), k)

print(_a * _b)
