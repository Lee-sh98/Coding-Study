import sys
input = sys.stdin.readline

def bs(arr, target):
    l, r = 0, len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0]*(N+1)

for i in range(N):
    C[A[i]] = i

for i in range(N):
    B[i] = C[B[i]]

answer = [B[0]]
for i in range(1, N):
    if answer[-1] < B[i]:
        answer.append(B[i])
    else:
        idx = bs(answer, B[i])
        answer[idx] = B[i]

print(len(answer))
