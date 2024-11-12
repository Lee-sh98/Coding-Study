import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(cur,select):
    if dp[cur][select] != -1:
        return dp[cur][select]

    dp[cur][select] = point[cur]*select
    for child in children[cur]:
        dp[cur][select]+=max(solve(child, i) for i in range(2-select))
    return dp[cur][select]

N = int(input())
point = [0]+[*map(int, input().split())]
edges = [[] for _ in range(N+1)]
children = [[] for _ in range(N+1)]
dp = [[-1]*2 for _ in range(N+1)]

for _ in range(N-1):
    A,B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

stack = [1]
while stack:
    cur = stack.pop()
    for child in edges[cur]:
        if not children[child]:
            children[cur].append(child)
            stack.append(child)

print(max(solve(1, i) for i in range(2)))
