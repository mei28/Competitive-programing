n = int(input())


def send(a, b, c, d):
    print(f"? {a} {b} {c} {d}")
    a = int(input())
    return a


u = 1
d = n + 1
while d - u > 1:
    m = (u + d) // 2
    c = send(u, m - 1, 1, n)
    if c == m - u:
        u = m
    else:
        d = m
l = 1
r = n + 1
while r - l > 1:
    m = (r + l) // 2
    c = send(1, n, l, m - 1)
    if c == m - l:
        l = m
    else:
        r = m
print(f"! {u} {l}")
