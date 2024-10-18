import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

step = N//K

for i in range(0, N, step):
    arr[i:i+step] = sorted(arr[i:i+step])

print(*arr)
