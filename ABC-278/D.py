n = int(input())
A = list(map(int, input().split()))

q = int(input())

dct = dict()
all_sum = -1
for _ in range(q):
    l = input().split()

    if l[0] == "1":
        x = int(l[1])
        all_sum = x
        dct = dict()
        pass
    if l[0] == "2":
        i, x = int(l[1]), int(l[2])
        i -= 1
        dct[i] = dct.setdefault(i, 0) + x
        pass
    if l[0] == "3":
        i = int(l[1])
        i -= 1
        if all_sum < 0:
            if i in dct.keys():
                print(A[i] + dct[i])
            else:
                print(A[i])
        else:
            if i in dct.keys():
                print(all_sum + dct[i])
            else:
                print(all_sum)
