N = int(input())
A = [int(input()) for _ in range(N)]
B = A.copy()
B = sorted(B, reverse=True)

fst = B[0]
sec = B[1]
for a in A:
    if fst == a:
        print(sec)
    else:
        print(fst)
