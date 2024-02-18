n = int(input())
S = input()

for i in range(n - 2):
    if "ABC" == S[i : i + 3]:
        print(i + 1)
        exit()
print(-1)
