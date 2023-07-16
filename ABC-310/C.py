N = int(input())
sticks = set()
for _ in range(N):
    S = input().strip()
    # consider the lexicographically smaller one between the string and its reverse
    key = min(S, S[::-1])
    sticks.add(key)
print(len(sticks))
