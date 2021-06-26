a, b, x = map(int, input().split())


def f(n: int) -> int:
    # f(n) := 0以上n以下で条件を満たす個数
    if n >= 0:
        return n // x + 1
    elif n == -1:
        return 0


print(f(b) - f(a - 1))
