import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

arr = [[[0]*(len(C)+1) for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            if A[i]==B[j]==C[k]:
                arr[i+1][j+1][k+1] = arr[i][j][k] + 1
            else:
                arr[i+1][j+1][k+1] = max(arr[i][j+1][k+1], arr[i+1][j][k+1], arr[i+1][j+1][k])

print(arr[len(A)][len(B)][len(C)])        
