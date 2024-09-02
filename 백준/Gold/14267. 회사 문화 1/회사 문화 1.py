import sys
input = sys.stdin.readline

def calculate(cur):
    if parents[cur] == -1:
        return praised[cur]
    if answer[cur] != -1:
        return answer[cur]
    answer[cur] = praised[cur]+calculate(parents[cur])
    return answer[cur]

n, m = map(int, input().split())
parents = [-1] + list(map(int, input().split()))
praised = [0]*(n+1)

for _ in range(m):
    i, w = map(int, input().split())
    praised[i] += w

answer = [-1]*(n+1)
answer[1] = praised[1]
for i in range(2, n+1):
    calculate(i)

print(" ".join(map(str, answer[1:])))
