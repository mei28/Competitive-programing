s = input()

M = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

M = M[::-1]

for i, m in enumerate(M):
    if m == s:
        print(i + 1)
        exit()
