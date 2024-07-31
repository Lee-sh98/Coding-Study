import sys

N = int(sys.stdin.readline())
arr = [2]*(N+1)

for i in range(1, N+1):
    arr[i] = arr[i-1]*2 - 1

print(arr[N]*arr[N])
