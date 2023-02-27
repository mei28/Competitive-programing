import string

S = input()
alp = string.ascii_uppercase

for i, s in enumerate(S):
    if s in alp:
        print(i + 1)
        exit()
