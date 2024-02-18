n = int(input())

if n == 1:
    print(1)
    exit()


def divi(n: int):
    l = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # l.append(i)
            if i != n // i:
                l.append([i, n // i])
            else:
                l.append([i, i])
    l.sort()
    return l


l = divi(n)

ans = 10**11


def f(a, b):
    return max(len(str(a)), len(str(b)))


for i, j in l:
    ans = min(f(i, j), ans)

print(ans)
