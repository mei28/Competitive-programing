N = int(input())
r_dog = []
g_dog = []
b_dog = []
for i in range(2 * N):
    a, c = input().split()
    a = int(a)
    if c == "R":
        r_dog.append(a)
    elif c == "G":
        g_dog.append(a)
    elif c == "B":
        b_dog.append(a)


def solve(X, Y):
    ans = 3 * 10 ** 15
    x, y = 0, 0

    while x < len(X) and y < len(Y):
        if X[x] < Y[y]:
            ans = min(abs(Y[y] - X[x]), ans)
            x += 1
        else:
            ans = min(abs(X[x] - Y[y]), ans)
            y += 1
    return ans


def main():
    r_dog.sort()
    g_dog.sort()
    b_dog.sort()

    if len(r_dog) % 2 == 0 and len(g_dog) % 2 == 0 and len(b_dog) % 2 == 0:
        print(0)
        return 0

    rg = solve(r_dog, g_dog)
    gb = solve(g_dog, b_dog)
    br = solve(b_dog, r_dog)

    if len(r_dog) % 2 == 0:
        print(min(gb, rg + br))
        return 0
    if len(g_dog) % 2 == 0:
        print(min(br, rg + gb))
        return 0
    if len(b_dog) % 2 == 0:
        print(min(rg, gb + br))
        return 0


if __name__ == "__main__":
    main()
