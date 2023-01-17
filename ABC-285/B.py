n = int(input())
S = input()

for i in range(1, n):
    cnt = 0
    for j in range(n):
        if j + i < n and S[j] != S[j + i]:
            cnt += 1
        else:
            break
    print(cnt)
