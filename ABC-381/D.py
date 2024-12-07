def solve(N, A):
    max_length = 0
    counts = {}
    left = 0
    i = 0
    while i + 1 < N:
      
        if A[i] == A[i + 1]:
            num = A[i]
            counts[num] = counts.get(num, 0) + 2
         
            while counts[num] > 2:
                counts[A[left]] -= 2
                if counts[A[left]] == 0:
                    del counts[A[left]]
                left += 2
          
            max_length = max(max_length, i + 2 - left)
            i += 2
        else:
      
            counts.clear()
            i+= 1
            left = i
    return max_length

N =int(input())
A= list(map(int, input().split()))
result = solve(N, A)
print(result)

