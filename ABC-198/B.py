N = input()

cnt = 0

for i in N[::-1]:
    if i == "0":
        cnt += 1
    else:
        break

N = "0" * cnt + N

for i in range(-(-len(N) // 2)):
    a = N[i]
    b = N[-i - 1]
    if a != b:
        print("No")
        exit()

print("Yes")
