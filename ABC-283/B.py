n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    l = input().split()
    if l[0] == "1":
        a = int(l[1])
        b = int(l[2])
        A[a - 1] = b
    else:
        a = int(l[1])
        print(A[a - 1])
