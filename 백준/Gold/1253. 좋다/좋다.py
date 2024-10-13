import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
result = 0

for i in range(N):
    l, r = 0, N-1
    while l<r:
        if l==i:
            l+=1
            continue
        if r==i:
            r-=1
            continue
        s = A[l] + A[r]
        if s==A[i]:
            result += 1
            break
        if s > A[i]:
            r -= 1
        else:
            l += 1
        
print(result)
