s = input()

ans = ''

for i in s:
    if i=='0':
        ans += '0'
    elif i=='1':
        ans += '1'
    else:
        ans = ans[:-1]

print(ans)
