K, A, B = map(int,input().split())

if B-A <=2:
    print(K+1)
else:
    bis = 1

    bis += A-1
    K -= A-1

    bis += (K//2)*(B-A)
    K = K%2

    bis +=K

    print(bis)
