n = input()
if int(n)>=42:
    n = str( int(n)+1 )
if len(n)>2:
    print("AGC"+n)
elif len(n)>1:
    print("AGC0"+n)
else:
    print("AGC00"+n)

