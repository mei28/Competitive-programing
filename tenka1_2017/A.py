N = int(input())

for h in range(1, 3501):
    for n in range(h, 3501):
        # 4hnw = N(nw+hw+hn)
        # w(4hn-Nn-Nh) = Nhn
        # w = Nhn/(4hn-Nn-Nh)
        if 4 * h * n - N * n - N * h != 0:
            w = N * h * n / (4 * h * n - N * n - N * h)

            if int(w) == w and 0 < w < 3501:
                print(h, n, int(w))
                exit(0)
