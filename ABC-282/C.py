n = int(input())
S = input().split('"')
print('"'.join([s if i % 2 else s.replace(",", ".") for i, s in enumerate(S)]))
