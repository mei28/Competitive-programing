n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AA = [(a, "a") for a in A]
BB = [(b, "b") for b in B]
CC = AA + BB

CC.sort()

ans_A = []
ans_B = []

for i, c in enumerate(CC):
    i += 1
    if c[1] == "a":
        ans_A.append(i)
    elif c[1] == "b":
        ans_B.append(i)
    else:
        raise ValueError
print(*ans_A)
print(*ans_B)
