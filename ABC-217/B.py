S = ["ABC", "ARC", "AGC", "AHC"]
I = []
for i in range(3):
    s = input()
    I.append(s)

print(*list(set(S) - set(I)))
