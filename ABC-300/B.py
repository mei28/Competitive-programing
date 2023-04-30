h, w = map(int, input().split())
A = [input() for _ in range(h)]
B = [input() for _ in range(h)]
AA = [a + a[::] for a in A]
AA = AA + AA[::]


for s in range(h):
    for t in range(w):
        tmp = []
        for i in range(h):
            _tmp = []
            for j in range(w):
                _tmp += A[(s + i) % h][(t + j) % w]
            tmp.append("".join(_tmp))
        if tmp == B:
            print("Yes")
            exit()
print("No")
