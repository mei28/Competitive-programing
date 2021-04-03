from collections import Counter

H, W = map(int, input().split())
A = []

for i in range(H):
    l = input()
    A += l


c = Counter(A)

if c["#"] != H + W - 1:
    print("Impossible")
else:
    print("Possible")
