import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr += [arr[0]]

A, B = 0, 0
for i in range(N):
    A += arr[i][0]*arr[i+1][1]
    B += arr[i][1]*arr[i+1][0]

print(round(abs(A-B)/2, 2))
