n = int(input())
s = input()


for i, j in enumerate(s):
    if j == "1":
        if i % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")
        exit()
