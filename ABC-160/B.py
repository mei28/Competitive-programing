X = int(input())

cnt = 0

cnt += 1000*(X//500)
X -= 500*(X//500)

cnt += 5*(X//5)

print(cnt)
