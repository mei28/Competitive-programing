S = input()
k = int(input())


ok = 0
ng = len(S) + 1

A = [0]*(len(S)+1)
for i in range(len(S)):
    A[i+1] = A[i]
    if S[i]==".":
        A[i+1] += 1

def check(ans:int)->bool:
    """
    kこ書き換えて連続してansすることがあるか
    """
    for i in range(len(S)-ans+1):
        if A[i+ans] - A[i] <= k:
            return True
    return False





while ng-ok>1:
    m = (ok+ng)//2

    if check(m):
        ok = m
    else:
        ng = m

print(ok)
