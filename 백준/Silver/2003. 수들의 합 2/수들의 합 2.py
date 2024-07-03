import sys
input = sys.stdin.readline

answer = 0
total = 0
end = 0
N, M = map(int, input().split())
arr = list(map(int, input().split()))

for cur in arr:
    while end<N and total<M:
        total+=arr[end]
        end += 1
    if total == M:
        answer += 1
    if total >= M:
        total -= cur

print(answer)
