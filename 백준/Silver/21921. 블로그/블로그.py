import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0]*(N+1)
for i in range(N):
    acc[i+1] = acc[i] + arr[i]

result = 0
count = 0

for i in range(N-X+1):
    cur = acc[i+X] - acc[i]

    if cur == result:
        count += 1
    elif cur > result:
        result = cur
        count = 1

if result:
    print(result)
    print(count)
else:
    print("SAD")
