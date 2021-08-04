S = input()
zone = "ZONe"
cnt = 0
for i in range(0, len(S) - 3):
    if S[i : i + 4] == zone:
        cnt += 1

print(cnt)
