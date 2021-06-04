def f(x: int) -> int:
    str_x = str(x)
    y = sum(int(a) for a in str_x)
    return (x + y) % 100000


if __name__ == "__main__":
    n, k = map(int, input().split())

    calculator = [n]

    for i in range(10 ** 5 + 100):
        nxt = f(calculator[-1])
        calculator.append(nxt)

    if k < 10 ** 5:
        ans = n
        for i in range(k):
            ans = f(ans)
        print(ans)

    else:
        loop_end = 100000
        loop_start = loop_end - 1
        while calculator[loop_end] != calculator[loop_start]:
            loop_start -= 1
        period = loop_end - loop_start
        idx = calculator.index(calculator[loop_start])

        k -= idx

        k %= period
        print(calculator[idx + k])
