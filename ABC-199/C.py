if __name__ == "__main__":
    n = int(input())
    S = list(input())
    q = int(input())

    flip = False

    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            if flip:
                a = (a + n) % (2 * n)
                b = (b + n) % (2 * n)
            S[b], S[a] = S[a], S[b]
        else:
            flip = not flip

    ans = ""
    if flip:
        ans = "".join(S[n:]) + "".join(S[:n])
    else:
        ans = "".join(S[:n]) + "".join(S[n:])

    print(ans)
