N, M, T = map(int, input().split())
A, B = [], []

for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

N_now = N
a_old = 0
b_last = 0
for a, b in zip(A, B):
    diff_t = a - b_last
    if N_now == N and diff_t == 1:
        continue
    if N_now - diff_t <= 0:
        print("No")
        exit()
    N_now = N_now - diff_t

    diff = b - a
    N_now = min(N_now + diff, N)

    b_last = b
diff_t = T - b_last

if N_now - diff_t > 0:
    print("Yes")
    exit()

else:
    print("No")
