N, D, H = map(int, input().split())
ans = 0


def f(x_, y_, x=0):
    y = (y_ - H) * (x - D) / (x_ - D) + H
    return y


for i in range(N):
    d, h = map(int, input().split())
    ans = max(ans, f(d, h))


print(f"{ans:.20f}")
