n = int(input())


res:str = ''

while n>0:
    n-=1
    res += chr( ord('a') + (n%26) )
    n //= 26

res = res[::-1]
print(res)
