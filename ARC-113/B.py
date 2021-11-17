a, b, c = map(int, input().split())

a %= 10

loop = 2
while a!=pow(a,loop,10):
    loop += 1

bc = pow(b,c,loop-1)
if bc==0:
    bc = loop-1
print(pow(a,bc,10))
