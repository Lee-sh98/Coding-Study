import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

n, m = len(A), len(B)

arr = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

print(arr[n][m])
