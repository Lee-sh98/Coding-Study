import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
acc = [0]*(N+1)
for i in range(1, N):
    acc[i] = acc[i-1] + (score[i] < score[i-1])

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(acc[y-1]-acc[x-1])
