# T = int(input())


# def solve(n, s, k):
#     for i in range(10 ** 8):
#         if (s + k * i) % n == 0:
#             return i
#     return -1


# N, S, K = [], [], []

# for t in range(T):
#     n, s, k = map(int, input().split())
#     N.append(n)
#     S.append(s)
#     K.append(k)

# for i in range(T):
#     n = N[i]
#     s = S[i]
#     k = K[i]
#     print(solve(n, s, k))


def euclid(x, y):
    if y == 0:
        return (0, 1, y)
    else:
        (A, B, g) = euclid(y, y % x)
        return (-B * (y // x), A + B, g)


t = int(input())

for _ in range(t):
    n, s, k = map(int, input().split())
    (a, b, g) = euclid(k, n)
    if (-s - 1) % g == 0:
        print(-1)
        exit()

    a *= (-s - 1) // g
    b *= (-s - 1) // g
    a %= n // g
    print(a)
