n,m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))

#sに1種類の数字しかない
if len(set(s))==1:
  if len(set(t)) == 1:
    if s[0] != t[0]:
      print(-1)
    else:
      print(len(t))
  else:
    print(-1)

#sに0,1両方ある
else:
  ans = m
  if len(set(t)) == 2:
    s2 = s + s
    stay = s2[n]
    tmp = -1
    while tmp == -1:
      for i in range(n):
        if s2[n+i] != stay:
          tmp = i
          break
        elif s2[n-i] != stay:
          tmp = i
          break
    #print(tmp)
    ans += tmp-1
    #異なる数字を使うにはtmp回のシフトが必要
    if t[0] != stay:
      ans += 1
    if m == 1:
      print(ans)
    else:
      for i in range(1,m):
        if t[i-1] != t[i]:
          ans += 1
      print(ans)
  
  else:
    s2 = s + s
    stay = s2[n]
    if t[0] == stay:
      print(ans)
    
    else:
      tmp = -1
      while tmp == -1:
        for i in range(n):
          if s2[n+i] != stay:
            tmp = i
            break
          elif s2[n-i] != stay:
            tmp = i
            break
      ans += tmp
      print(ans)
