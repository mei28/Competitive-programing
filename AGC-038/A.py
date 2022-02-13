h,w,a,b = map(int,input().split())

for i in range(h):
    for j in range(w):
        if i<b and j<a:
            print('0', end='')
        elif i>=b and j>=a:
            print('0',end ='')
        else:
            print('1',end = '')

    print('')
