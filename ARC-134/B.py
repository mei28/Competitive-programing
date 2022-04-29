import heapq

n = int(input())
S = list(input())
S_num = [ord(s)-ord('a') for s in S]

que = [(x,-i) for i, x in enumerate(S_num)]
heapq.heapify(que)

l,r = 0,n

while l<r:
    x,i = heapq.heappop(que)
    i *= -1

    if i<= r:
        while l<r and S[l] == S[i]:
            l += 1
        if l < i:
            S[l],S[i] = S[i], S[l]
            l += 1
            r = i-1

print(''.join(S))
