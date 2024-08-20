import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
acc = [0]*(N+1)

for i in range(N):
    acc[i+1] = acc[i] + arr[i]

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(acc[j]- acc[i-1])
