a, b = map(int, input().split())


def uruu(n: int) -> int:
    """nまでの閏年の数"""
    ans: int = n // 4 - n // 100 + n // 400
    return ans


print(uruu(b) - uruu(a - 1))
