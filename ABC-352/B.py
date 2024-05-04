S = input()
T = input()

j = 0

for s in S:
    while j < len(T):
        if s == T[j]:
            print(j + 1, end=" ")
            j += 1
            break
        j += 1
