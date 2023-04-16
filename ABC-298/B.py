import numpy as np

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
AA = np.array(A)
BB = np.array(B)


def check(_A, _B):
    for i in range(n):
        for j in range(n):
            if _A[i][j] == 1 and _B[i][j] != 1:
                return False
    return True


for i in range(4):
    AAA = np.rot90(AA, -i)
    if check(AAA, BB):
        print("Yes")
        exit()
print("No")
