S = input()
k = int(input())


ok = 0
ng = len(S) + 1

def check(ans:int)->bool:
    """
    kこ書き換えて連続してansすることがあるか
    """
    for i in range(len(S)-ans+1):
        tmp = S[i:i+ans]
        if tmp.count('.') <= k:
            return True
    return False





while ng-ok>1:
    m = (ok+ng)//2

    if check(m):
        ok = m
    else:
        ng = m

print(ok)
