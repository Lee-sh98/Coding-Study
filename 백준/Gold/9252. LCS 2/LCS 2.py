import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

n, m = len(A), len(B)

arr = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if A[i] == B[j]:
            arr[i+1][j+1] = arr[i][j]+1
        else:
            arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])

x, y = n, m
result = ""
while True:
    if x==0 or y==0:
        break
    if A[x-1] == B[y-1]:
        result += A[x-1]
        x -= 1
        y -= 1
    else:
        if arr[x][y-1] > arr[x-1][y]:
            y -= 1
        else:
            x -= 1
    
print(arr[n][m])
print(result[::-1])
