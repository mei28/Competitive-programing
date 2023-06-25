H_A, W_A = map(int, input().split())
A = [list(input()) for _ in range(H_A)]

H_B, W_B = map(int, input().split())
B = [list(input()) for _ in range(H_B)]

H_X, W_X = map(int, input().split())
X = [list(input()) for _ in range(H_X)]

H_C = H_A + H_B
W_C = W_A + W_B
CAs = []
CBs = []


def show(AA):
    print("=" * 20)
    for a in AA:
        print("".join(a))


for i in range(H_C - H_A):
    for j in range(W_C - W_A):
        C = [["." for _ in range(W_C + 1)] for _ in range(H_C + 1)]
        for ai in range(H_A):
            for aj in range(W_A):
                C[i + ai + 1][j + aj + 1] = A[ai][aj]
        CAs.append(C)
for i in range(H_C - H_B):
    for j in range(W_C - W_B):
        C = [["." for _ in range(W_C + 1)] for _ in range(H_C + 1)]
        for ai in range(H_B):
            for aj in range(W_B):
                C[i + ai + 1][j + aj + 1] = B[ai][aj]
        CBs.append(C)

Cs = []
for i in range(len(CAs)):
    for j in range(len(CBs)):
        C = [["." for _ in range(W_C + 1)] for _ in range(H_C + 1)]
        for k in range(H_C):
            for l in range(W_C):
                if CAs[i][k][l] == "#":
                    C[k][l] = "#"
                if CBs[j][k][l] == "#":
                    C[k][l] = "#"
        Cs.append(C)


def check(C):
    for i in range(H_C + 1 - H_X):
        for j in range(W_C + 1 - W_X):
            tmp = [["." for _ in range(W_X)] for _ in range(H_X)]
            for xi in range(H_X):
                for xj in range(W_X):
                    tmp[xi][xj] = C[i + xi][j + xj]

            if tmp == X:
                return True
    return False


cnt_A, cnt_B = 0, 0
cnt_X = 0

for a in A:
    cnt_A += a.count("#")
for b in B:
    cnt_B += b.count("#")

for x in X:
    cnt_X += x.count("#")

if max(cnt_A, cnt_B) > cnt_X:
    print("No")
    exit()

for C in Cs:
    if check(C):
        print("Yes")
        exit()
print("No")
