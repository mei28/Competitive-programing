n = int(input())
S = input()

for i in range(n):
    if S[i : i + 2] == "ab" or S[i : i + 2] == "ba":
        print("Yes")
        exit()
print("No")
