S = input()
n = len(S)


T = "oxx" * 1000

for i in range(len(T) - n):
    tmp = T[i : i + n]
    if tmp == S:
        print("Yes")
        exit()

print("No")
