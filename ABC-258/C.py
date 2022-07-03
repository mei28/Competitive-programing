n, q = map(int, input().split())
S = input()

cnt = 0
for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        cnt += b
    else:
        c = cnt % n
        c += 1
        print(S[b-c])
