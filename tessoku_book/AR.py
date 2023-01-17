n, q = map(int, input().split())

A = [i + 1 for i in range(n)]
rev = False
for _ in range(q):
    l = input().split()
    if l[0] == "1":
        x, y = map(int, l[1:])
        if rev:
            A[-x] = y
        else:
            A[x - 1] = y
    elif l[0] == "2":
        rev = not rev
    else:
        x = int(l[1])
        if rev:
            print(A[-x])
        else:
            print(A[x - 1])
