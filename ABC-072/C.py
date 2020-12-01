N = int(input())
A = list(map(int, input().split()))

dic = {}

for a in A:
    dic[a] = dic.setdefault(a, 0)+1
    dic[a - 1] = dic.setdefault(a-1, 0) + 1
    dic[a+1] = dic.setdefault(a+1, 0) + 1

print(max(dic.values()))
