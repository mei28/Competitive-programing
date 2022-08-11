from itertools import count


def calc_odd_factor_prod(n):
    """次数が奇数の素因数の積を得る（わかりづらかったら、普通に素因数分解して、次数が奇数のものをかけ合わせてください"""
    for i2 in (i * i for i in count(2)):
        if i2 > n:
            break
        while n % i2 == 0:
            n //= i2
    return n


def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        odd = calc_odd_factor_prod(i)
        for j in range(1, N + 1):
            if odd * j * j > N:
                break
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
