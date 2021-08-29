n = int(input())
ST = []
for i in range(n):
    s, t = input().split()
    ST.append([s, t])

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if ST[i][0] == ST[j][0] and ST[i][1] == ST[j][1]:
            print("Yes")
            exit()

print("No")
