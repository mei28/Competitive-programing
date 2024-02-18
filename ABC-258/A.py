k = int(input())

h = k // 60
m = k % 60

h = 21 + h

h %= 24
print(f"{h}:{m:02}")
